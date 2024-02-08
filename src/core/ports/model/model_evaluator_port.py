from abc import ABC, abstractmethod
from typing import List, Dict

from ....core.entities.model.base_model_entity import BaseModelEntity
from ....core.entities.data.processed_data_entity import ProcessedDataEntity

class ModelEvaluatorPort(ABC):
  @abstractmethod
  def evaluate_model_training(self, model: BaseModelEntity, test_data: ProcessedDataEntity) -> Dict[str, float]:
    pass
  
  @abstractmethod
  def evaluate_model_embedding(self, model: BaseModelEntity, test_data: ProcessedDataEntity, threshold: float) -> Dict[str, float]:
    pass