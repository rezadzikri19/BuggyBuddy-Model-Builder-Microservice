from ...ports.data.data_loader_port import DataLoaderPort
from ...ports.logger_port import LoggerPort

from ...entities.data.extracted_data_entity import ExtractedDataEntity
from ...entities.data.embedded_data_entity import EmbeddedDataEntity

from ...utils.schema_validation_util import io_schema_validation

class LoadDataUsecase():
  def __init__(
      self,
      data_loader: DataLoaderPort,
      logger: LoggerPort) -> None:
    self.data_loader = data_loader
    self.logger = logger
    
  
  @io_schema_validation(schema_input=ExtractedDataEntity())
  def dump_extracted_data(self, data: ExtractedDataEntity):
    try:
      self.data_loader.dump_extracted_data(data)
    except Exception as error:
      error_message = f'LoadDataUsecase.dump_extracted_data: {error}'
      self.logger.log_error(error_message, error)
        
  
  @io_schema_validation(schema_input=EmbeddedDataEntity())
  def dump_loaded_data(self, data: EmbeddedDataEntity):
    try:
      self.data_loader.dump_loaded_data(data)
    except Exception as error:
      error_message = f'LoadDataUsecase.dump_loaded_data: {error}'
      self.logger.log_error(error_message, error)