from ....core.ports.model.model_saver_port import ModelSaverPort
from ....core.ports.logger_port import LoggerPort

from ....core.entities.model.base_model_entity import BaseModelEntity


class ModelSaveUsecase:
  def __init__(
      self,
      model_saver: ModelSaverPort,
      logger: LoggerPort) -> None:
    self.model_saver = model_saver
    self.logger = logger
  
  
  def save_models(
      self,
      model_training: BaseModelEntity,
      model_embedding: BaseModelEntity) -> None:
    try:
      self.model_saver.save_model_training(model_training)
      self.model_saver.save_model_embedding(model_embedding)
    except Exception as error:
      error_message = f'ModelSaveUsecase.save_models: {error}'
      self.logger.log_error(error_message, error)