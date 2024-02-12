from ....core.ports.model.model_creator_port import ModelCreatorPort
from ....core.ports.logger_port import LoggerPort

from ....core.entities.model.base_model_entity import BaseModelEntity

class ModelCreateUsecase:
  def __init__(
      self,
      model_creator: ModelCreatorPort,
      logger: LoggerPort) -> None:
    self.model_creator = model_creator
    self.logger = logger
  
  
  def create_models(self) -> BaseModelEntity:
    try:
      model_training = self.model_creator.create_model_training(model=None)
      return model_training
    except Exception as error:
      error_message = f'ModelCreateUsecase.create_models: {error}'
      self.logger.log_error(error_message, error)
    