from ...ports.data.data_preprocessor_port import DataPreprocessorPort
from ...ports.logger_port import LoggerPort

from ...utils.schema_validation_util import io_data_validation

from ...entities.data.extracted_data_entity import ExtractedDataEntity
from ...entities.data.preprocessed_data_entity import *

class PreprocessDataUsecase:
  def __init__(
      self,
      data_preprocessor: DataPreprocessorPort,
      logger: LoggerPort) -> None:
    self.data_preprocessor = data_preprocessor
    self.logger = logger
  
  
  @io_data_validation(schema_input=ExtractedDataEntity(), schema_output=PreprocessedDataEntity())
  def preprocess_data(self, data: ExtractedDataEntity) -> PreprocessedDataEntity:
    try:
      features_to_drop = ['id', 'status', 'priority', 'resolution', 'severity', 'component', 'product', 'type']
      
      result = self.data_preprocessor.drop_features(data, features_to_drop=features_to_drop)
      result = self.data_preprocessor.remove_duplicates(data, keep='first')
      result = self.data_preprocessor.aggregate_text_features(data)
      result = self.data_preprocessor.clean_sentences(data)
      result = self.data_preprocessor.remove_stopwords(data)
      result = self.data_preprocessor.generate_sent_embeddings(data)
      result = self.data_preprocessor.generate_sent_pairs(data)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.preprocess_data: {error}'
      self.logger.log_error(error_message, error)