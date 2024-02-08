from typing import List, Dict, Tuple

from ....core.ports.model.model_evaluator_port import Model_Evaluator
from ....core.entities.model.base_model_entity import BaseModelEntity
from ....core.entities.data.processed_data_entity import ProcessedDataEntity

class ModelEvaluateUsecase:
  def __init__(self, model_evaluator: Model_Evaluator) -> None:
    self.model_evaluator = model_evaluator
  
  
  def evaluate_model_training(
      self,
      model_training: BaseModelEntity,
      model_embedding: BaseModelEntity,
      test_data: ProcessedDataEntity) -> Tuple[List[Dict[str, float]]]:
    metrics_training = self.model_evaluator.evaluate_model_training(model_training, test_data=test_data)
    metrics_embedding = self.model_evaluator.evaluate_model_embedding(model_embedding, test_data=test_data)
    
    return (metrics_training, metrics_embedding)