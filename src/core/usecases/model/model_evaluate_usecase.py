from typing import Tuple

from ....core.ports.model.model_evaluator_port import ModelEvaluatorPort
from ....core.ports.logger_port import LoggerPort

from ....core.entities.model.base_model_entity import BaseModelEntity
from ....core.entities.data.preprocessed_data_entity import PreprocessedDataEntity

from ....core.dtos.model.model_evaluate_dto import ModelMetricsDTO

class ModelEvaluateUsecase:
  def __init__(
      self,
      model_evaluator: ModelEvaluatorPort,
      logger: LoggerPort) -> None:
    self.model_evaluator = model_evaluator
    self.logger = logger
  
  
  def evaluate_models(
      self,
      model_training: BaseModelEntity,
      model_embedding: BaseModelEntity,
      test_data: PreprocessedDataEntity,
      similarity_threshold: float = 0.5) -> Tuple[ModelMetricsDTO]:
    try:
      metrics_training = self.model_evaluator.evaluate_model_training(model_training, test_data)
      metrics_embedding = self.model_evaluator.evaluate_model_embedding(model_embedding, test_data, similarity_threshold)
      return (metrics_training, metrics_embedding)
    except Exception as error:
      error_message = f'ModelEvaluateUsecase.evaluate_models: {error}'
      self.logger.log_error(error_message, error)