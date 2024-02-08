from ...core.entities.model.base_model_entity import BaseModelEntity
from ...core.ports.model.model_creator_port import ModelCreatorPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.model_wrapper_util import keras_model_wrapper

import tensorflow.keras as keras
from keras.models import Model
from keras.layers import Dense, Input, Dot

class ModelCreatorDriver(ModelCreatorPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
    
  
  @keras_model_wrapper
  def create_model_training(self) -> BaseModelEntity:
    input_1 = Input(shape=(384, ), name='input_1')
    input_2 = Input(shape=(384, ), name='input_2')

    shared_node_1 = Dense(256, name='shared_node_1')
    shared_node_2 = Dense(256, name='shared_node_2')
    shared_node_3 = Dense(128, name='shared_node_3')
    shared_node_4 = Dense(128, name='shared_node_4')

    x1 = shared_node_1(input_1)
    x1 = shared_node_2(x1)
    x1 = shared_node_3(x1)
    x1 = shared_node_4(x1)

    x2 = shared_node_1(input_2)
    x2 = shared_node_2(x2)
    x2 = shared_node_3(x2)
    x2 = shared_node_4(x2)

    cosine_similarity_layer = Dot(axes=-1, normalize=True, name='cosine_similarity')([x1, x2])
    output_layer = Dense(1, activation='sigmoid', name='output')(cosine_similarity_layer)

    model_training = Model(inputs=[input_1, input_2], outputs=output_layer, name='training_model')

    optimizer = keras.optimizers.Adam(learning_rate=0.002)
    loss = keras.losses.BinaryCrossentropy(from_logits=False)

    model_training.compile(loss=loss, optimizer=optimizer, metrics=[keras.metrics.Precision(), keras.metrics.Recall()])
    return model_training
  
  
  @keras_model_wrapper
  def create_model_embedding(self, model: BaseModelEntity) -> BaseModelEntity:
    input_ = Input(shape=(384, ), name='input')
    hidden = model.get_layer('shared_node_1')(input_)
    hidden = model.get_layer('shared_node_2')(hidden)
    hidden = model.get_layer('shared_node_3')(hidden)
    output_ = model.get_layer('shared_node_4')(hidden)

    embedding_model = Model(inputs=input_, outputs=output_, name='embd_inference_model')
    return embedding_model
