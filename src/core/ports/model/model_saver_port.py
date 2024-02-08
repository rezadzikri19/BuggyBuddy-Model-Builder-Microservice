from abc import ABC, abstractmethod

from ...entities.model.base_model_entity import BaseModelEntity

class ModelSaverPort(ABC):
  @abstractmethod
  def save_model_training(self, model: BaseModelEntity) -> None:
    pass
  
  @abstractmethod
  def save_model_embedding(self, model: BaseModelEntity) -> None:
    pass