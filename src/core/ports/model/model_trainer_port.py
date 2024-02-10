from typing import Tuple, Optional
from abc import ABC, abstractmethod

from ....core.entities.data.preprocessed_data_entity import PreprocessedDataEntity
from ....core.entities.model.base_model_entity import BaseModelEntity

class ModelTrainer(ABC):
  @abstractmethod
  def split_train_test_data(self, data: PreprocessedDataEntity, test_ratio: float = 0.2) -> Tuple(PreprocessedDataEntity, PreprocessedDataEntity):
    pass
  
  @abstractmethod
  def train_model_training(self, model: BaseModelEntity, train_data: PreprocessedDataEntity, valid_data: Optional[PreprocessedDataEntity] = None) -> None:
    pass
  
  @abstractmethod
  def get_similarity_threshold(self, model: BaseModelEntity, data: PreprocessedDataEntity) -> float:
    pass