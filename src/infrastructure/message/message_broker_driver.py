import pika
import json

from typing import Callable, Dict, Any

from ...core.ports.notification_port import NotificationPort

class RabbitMQMessageBrokerDriver(NotificationPort):
  _connection = None

  def __init__(self, host: str) -> None:
    if not RabbitMQMessageBrokerDriver._connection:
        RabbitMQMessageBrokerDriver._connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    self.connection = RabbitMQMessageBrokerDriver._connection
  
  
  def subscribe_topic(self, topic: str, callback: Callable[[bytes], None]) -> None:
    channel = self.connection.channel()
    channel.exchange_declare(exchange='etl_pipeline', exchange_type='direct')
    
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    
    subs_callback = lambda ch, method, properties, body: callback(json.loads(body.decode('utf-8')))
    
    channel.queue_bind(exchange='etl_pipeline', queue=queue_name, routing_key=topic)
    channel.basic_consume(queue=queue_name, on_message_callback=subs_callback, auto_ack=True)
    channel.start_consuming()

  
  def publish_message(self, topic: str, data: Dict[str, Any]) -> None:
    message_body = json.dumps(data)
    channel = self.connection.channel()
    
    channel.exchange_declare(exchange='train_pipeline', exchange_type='direct')
    channel.basic_publish(exchange='train_pipeline', routing_key=topic, body=message_body)
    
    
  def close(self) -> None:
    self.connection.close()
    RabbitMQMessageBrokerDriver._connection = None
