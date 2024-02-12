from abc import ABC, abstractmethod

from ...entities.model.base_model_entity import BaseModelEntity

class ModelCreatorPort(ABC):
  @abstractmethod
  def create_model_training(self, model: None = None) -> BaseModelEntity:
    pass
  
  @abstractmethod
  def create_model_embedding(self, model: BaseModelEntity) -> BaseModelEntity:
    pass