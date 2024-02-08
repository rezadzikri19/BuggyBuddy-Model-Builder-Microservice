from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

from ...entities.model.base_model_entity import BaseModelEntity

class ModelSaverPort(ABC):
  @abstractmethod
  def save_model_training(self, model: BaseModelEntity, metadata: Optional[Dict[str, Any]] = None) -> None:
    pass
  
  @abstractmethod
  def save_model_embedding(self, model: BaseModelEntity, metadata: Optional[Dict[str, Any]] = None) -> None:
    pass