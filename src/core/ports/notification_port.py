from typing import Callable, Dict, Any
from abc import ABC, abstractmethod

class NotificationPort(ABC):
  @abstractmethod
  def publish_message(self, topic: str, data: Dict[str, Any]) -> None:
    pass
  
  @abstractmethod
  def subscribe_topic(self, topic: str, callback: Callable[[Dict[str, Any]], None]) -> None:
    pass