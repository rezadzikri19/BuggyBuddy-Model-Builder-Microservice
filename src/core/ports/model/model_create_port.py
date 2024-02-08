from typing import Any
from abc import ABC, abstractmethod

from ....core.entities.model.base_model_entity import BaseModelEntity

class ModelCreatorPort(ABC):
  @abstractmethod
  def create_model(self, model: Any) -> BaseModelEntity:
    pass