from ...ports.data.data_preprocessor_port import DataPreprocessorPort
from ...ports.logger_port import LoggerPort

from ...utils.schema_validation_util import io_schema_validation

from ...entities.data.extracted_data_entity import ExtractedDataEntity
from ...entities.data.processed_data_entity import *


class PreprocessDataUsecase:
  def __init__(
      self,
      data_transformer: DataPreprocessorPort,
      logger: LoggerPort) -> None:
    self.data_transformer = data_transformer
    self.logger = logger
  
  
  @io_schema_validation(schema_input=ExtractedDataEntity(), schema_output=ProcessedDataEntity())
  def preprocess_data(self, data: ExtractedDataEntity) -> ProcessedDataEntity:
    try:
      features_to_drop = ['bug_id', 'status', 'priority', 'resolution', 'severity', 'component', 'product', 'report_type']
      
      result = self.data_transformer.drop_features(data, features_to_drop=features_to_drop)
      result = self.data_transformer.remove_duplicates(data, keep='first')
      result = self.data_transformer.aggregate_text_features(data)
      result = self.data_transformer.clean_sentences(data)
      result = self.data_transformer.remove_stopwords(data)
      result = self.data_transformer.generate_sent_embeddings(data)
      result = self.data_transformer.generate_sent_pairs(data)
      
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.preprocess_data: {error}'
      self.logger.log_error(error_message, error)