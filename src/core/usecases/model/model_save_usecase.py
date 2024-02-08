from ...ports.model.model_saver_port import ModelSaverPort
from ....core.entities.model.base_model_entity import BaseModelEntity

class ModelSaveUsecase:
  def __init__(self, model_saver: ModelSaverPort) -> None:
    self.model_saver = model_saver
  
  
  def save_model_training(self, model_training: BaseModelEntity, model_embedding: BaseModelEntity) -> None:
    self.model_saver.save_model_training(model_training)
    self.model_saver.save_model_embedding(model_embedding)