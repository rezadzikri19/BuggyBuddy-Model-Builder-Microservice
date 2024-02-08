from typing import Tuple, List, Dict
from abc import ABC, abstractmethod

from ....core.entities.data.processed_data_entity import ProcessedDataEntity
from ....core.entities.model.base_model_entity import BaseModelEntity

class ModelTrainer(ABC):
  @abstractmethod
  def split_train_test_data(self, data: ProcessedDataEntity) -> Tuple(ProcessedDataEntity, ProcessedDataEntity):
    pass
  
  @abstractmethod
  def train_model(self, data: ProcessedDataEntity, model: BaseModelEntity) -> None:
    pass
  
  @abstractmethod
  def evaluate_model(self, model: BaseModelEntity) -> List[Dict[str, float]]:
    pass