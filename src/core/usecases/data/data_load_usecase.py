from ...ports.data.data_loader_port import DataLoaderPort
from ...ports.logger_port import LoggerPort

from ...entities.data.embedded_data_entity import EmbeddedDataEntity

from ...utils.schema_validation_util import io_data_validation

class LoadDataUsecase():
  def __init__(
      self,
      data_loader: DataLoaderPort,
      logger: LoggerPort) -> None:
    self.data_loader = data_loader
    self.logger = logger
  
  
  @io_data_validation(schema_input=EmbeddedDataEntity())
  def dump_preprocessed_data(self, data: EmbeddedDataEntity):
    try:
      self.data_loader.dump_preprocessed_data(data)
    except Exception as error:
      error_message = f'LoadDataUsecase.dump_preprocessed_data: {error}'
      self.logger.log_error(error_message, error)
  
  
  @io_data_validation(schema_input=EmbeddedDataEntity())
  def dump_embedded_data(self, data: EmbeddedDataEntity):
    try:
      self.data_loader.dump_embedded_data(data)
    except Exception as error:
      error_message = f'LoadDataUsecase.dump_embedded_data: {error}'
      self.logger.log_error(error_message, error)