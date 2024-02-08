from ...core.ports.data_extractor_port import DataExtractorPort
from ...core.ports.logger_port import LoggerPort

from ...core.entities.extracted_data_entity import ExtractedDataEntity

from ...core.utils.schema_validation_util import io_schema_validation

class ExtractDataRawUsecase():
  def __init__(
      self,
      data_extractor: DataExtractorPort,
      logger: LoggerPort) -> None:
    self.data_extractor = data_extractor
    self.logger = logger
  
  
  @io_schema_validation(schema_output=ExtractedDataEntity())
  def fetch_data(self, data: None = None) -> ExtractedDataEntity:
    try:
      result = self.data_extractor.get_data_from_source(data=data)
      return result
    except Exception as error:
      error_message = f'ExtractDataRawUsecase.fetch_data: {error}'
      self.logger.log_error(error_message, error)

