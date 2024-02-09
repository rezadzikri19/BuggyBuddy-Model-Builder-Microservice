from abc import ABC, abstractmethod

from ....core.entities.model.base_model_entity import BaseModelEntity
from ...entities.data.preprocessed_data_entity import PreprocessedDataEntity

from ...dtos.model.model_evaluate_dto import ModelMetricsDTO

class ModelEvaluatorPort(ABC):
  @abstractmethod
  def evaluate_model_training(self, model: BaseModelEntity, test_data: PreprocessedDataEntity) -> ModelMetricsDTO:
    pass
  
  @abstractmethod
  def evaluate_model_embedding(self, model: BaseModelEntity, test_data: PreprocessedDataEntity, threshold: float) -> ModelMetricsDTO:
    pass