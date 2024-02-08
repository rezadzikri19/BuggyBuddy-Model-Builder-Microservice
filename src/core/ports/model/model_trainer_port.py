from typing import Tuple, List, Dict, Optional
from abc import ABC, abstractmethod

from ....core.entities.data.processed_data_entity import ProcessedDataEntity
from ....core.entities.model.base_model_entity import BaseModelEntity

class ModelTrainer(ABC):
  @abstractmethod
  def split_train_test_data(self, data: ProcessedDataEntity, test_ratio: int = 0.2) -> Tuple(ProcessedDataEntity, ProcessedDataEntity):
    pass
  
  @abstractmethod
  def train_model_training(self, model: BaseModelEntity, train_data: ProcessedDataEntity, valid_data: Optional[ProcessedDataEntity] = None) -> None:
    pass
  
  @abstractmethod
  def train_model_embedding(self, model: BaseModelEntity, data: ProcessedDataEntity) -> None:
    pass