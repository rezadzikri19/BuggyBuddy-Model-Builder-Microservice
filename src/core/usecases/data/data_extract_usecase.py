from ...ports.data.data_extractor_port import DataExtractorPort
from ...ports.logger_port import LoggerPort

from ...entities.data.extracted_data_entity import ExtractedDataEntity

from ...utils.schema_validation_util import io_schema_validation


class ExtractDataUsecase():
  def __init__(
      self,
      data_extractor: DataExtractorPort,
      logger: LoggerPort) -> None:
    self.data_extractor = data_extractor
    self.logger = logger
  
  
  @io_schema_validation(schema_output=ExtractedDataEntity())
  def fetch_data(self, data: None = None) -> ExtractedDataEntity:
    try:
      result = self.data_extractor.get_data_from_source(data)
      result = self.data_extractor.format_data(result)
      return result
    except Exception as error:
      error_message = f'ExtractDataUsecase.fetch_data: {error}'
      self.logger.log_error(error_message, error)

