from ....core.ports.data.data_extractor_port import DataExtractorPort
from ....core.ports.logger_port import LoggerPort

from ....core.entities.data.extracted_data_entity import ExtractedDataEntity
from ....core.entities.data.preprocessed_data_entity import PreprocessedDataEntity

from ....core.utils.schema_validation_util import io_data_validation

class ExtractDataUsecase():
  def __init__(
      self,
      data_extractor: DataExtractorPort,
      logger: LoggerPort) -> None:
    self.data_extractor = data_extractor
    self.logger = logger
  
  
  @io_data_validation(schema_output=ExtractedDataEntity())
  def fetch_data_from_source(self, data: None = None) -> ExtractedDataEntity:
    try:
      result = self.data_extractor.get_data_from_source(data)
      result = self.data_extractor.format_data(result)
      return result
    except Exception as error:
      error_message = f'ExtractDataUsecase.fetch_data_from_source: {error}'
      self.logger.log_error(error_message, error)

  
  @io_data_validation(schema_output=PreprocessedDataEntity())
  def fetch_cached_preprocessed_data(self, data: None = None) -> PreprocessedDataEntity:
    try:
      result = self.data_extractor.get_cached_preprocessed_data(data)
      return result
    except Exception as error:
      error_message = f'ExtractDataUsecase.fetch_cached_preprocessed_data: {error}'
      self.logger.log_error(error_message, error)

