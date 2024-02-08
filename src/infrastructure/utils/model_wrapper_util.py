from keras.models import Model

from ...core.entities.model.base_model_entity import BaseModelEntity

def keras_model_to_base_model(keras_model: Model) -> BaseModelEntity:
  base_model = BaseModelEntity(model=keras_model)
  return base_model


def base_model_to_keras_model(base_model: BaseModelEntity) -> Model:
  keras_model = base_model.model
  return keras_model


def keras_model_wrapper(func):
  def wrapper(self, model: BaseModelEntity, *args, **kwargs) -> BaseModelEntity:
    if model is not None:
      model = base_model_to_keras_model(model)
      
    model = func(self, model=model, *args, **kwargs)
    
    if model is not None:
      model = keras_model_to_base_model(model)
    return model
  return wrapper