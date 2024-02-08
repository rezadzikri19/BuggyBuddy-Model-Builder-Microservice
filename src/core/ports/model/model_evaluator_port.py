from abc import ABC, abstractmethod
from typing import List, Dict

from ....core.entities.model.base_model_entity import BaseModelEntity
from ....core.entities.data.processed_data_entity import ProcessedDataEntity

class Model_Evaluator(ABC):
  @abstractmethod
  def evaluate_model_training(self, model: BaseModelEntity, test_data: ProcessedDataEntity) -> List[Dict[str, float]]:
    pass
  
  @abstractmethod
  def evaluate_model_embedding(self, model: BaseModelEntity, test_data: ProcessedDataEntity) -> List[Dict[str, float]]:
    pass