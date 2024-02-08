from typing import Dict, Any

from ....core.ports.model.model_trainer_port import ModelTrainer
from ....core.ports.model.model_evaluator_port import Model_Evaluator
from ....core.ports.model.model_creator_port import ModelCreatorPort
from ....core.ports.logger_port import LoggerPort

from ....core.entities.model.base_model_entity import BaseModelEntity
from ....core.entities.data.processed_data_entity import ProcessedDataEntity


class ModelTrainUsecase:
  def __init__(
      self,
      model_trainer: ModelTrainer,
      model_evaluator: Model_Evaluator,
      model_creator: ModelCreatorPort,
      logger: LoggerPort) -> None:
    self.model_trainer = model_trainer
    self.model_evaluator = model_evaluator
    self.model_creator = model_creator
    self.logger = logger
  
  
  def train_models(
      self,
      model_training: BaseModelEntity,
      data: ProcessedDataEntity) -> Dict[str, Any]:
    try:
      train_data, valid_data = self.model_trainer.split_train_test_data(data, test_ratio=0.2)
      
      self.model_trainer.train_model_training(model_training, train_data=train_data, valid_data=valid_data)
      
      model_embedding = self.model_creator.create_model_embedding(model_training)
      similarity_threshold = self.model_trainer.get_similarity_threshold(model_embedding, data=data)
      
      return {
          'model_training': model_training,
          'model_embedding': model_embedding,
          'similarity_threshold': similarity_threshold
        }
    except Exception as error:
      error_message = f'ModelTrainUsecase.train_models: {error}'
      self.logger.log_error(error_message, error)