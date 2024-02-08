from typing import List, Dict, Tuple

from ....core.ports.model.model_evaluator_port import Model_Evaluator
from ....core.ports.logger_port import LoggerPort

from ....core.entities.model.base_model_entity import BaseModelEntity
from ....core.entities.data.processed_data_entity import ProcessedDataEntity


class ModelEvaluateUsecase:
  def __init__(
      self,
      model_evaluator: Model_Evaluator,
      logger: LoggerPort) -> None:
    self.model_evaluator = model_evaluator
    self.logger = logger
  
  
  def evaluate_models(
      self,
      model_training: BaseModelEntity,
      model_embedding: BaseModelEntity,
      test_data: ProcessedDataEntity) -> Tuple[List[Dict[str, float]]]:
    try:
      metrics_training = self.model_evaluator.evaluate_model_training(model_training, test_data=test_data)
      metrics_embedding = self.model_evaluator.evaluate_model_embedding(model_embedding, test_data=test_data)
      return (metrics_training, metrics_embedding)
    except Exception as error:
      error_message = f'ModelEvaluateUsecase.evaluate_models: {error}'
      self.logger.log_error(error_message, error)