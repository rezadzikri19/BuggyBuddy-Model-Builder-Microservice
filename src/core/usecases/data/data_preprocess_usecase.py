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
    

  @io_schema_validation(schema_input=ExtractedDataEntity(), schema_output=DropFeatsEntity())
  def drop_unused_features(self, data: ExtractedDataEntity) -> DropFeatsEntity:
    try:
      features_to_drop = ['status', 'priority', 'resolution', 'severity', 'component', 'product', 'report_type']
      
      result = self.data_transformer.drop_features(data, features_to_drop=features_to_drop)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.drop_features: {error}'
      self.logger.log_error(error_message, error)
  
  
  @io_schema_validation(schema_input=DropFeatsEntity(), schema_output=RemoveDuplicatesEntity())
  def remove_duplicates(self, data: DropFeatsEntity, keep: str = 'first') -> RemoveDuplicatesEntity:
    try:
      result = self.data_transformer.remove_duplicates(data, keep=keep)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.remove_duplicates: {error}'
      self.logger.log_error(error_message, error)


  @io_schema_validation(schema_input=RemoveDuplicatesEntity(), schema_output=AggregateTextEntity())
  def aggregate_text_features(self, data: RemoveDuplicatesEntity) -> AggregateTextEntity:
    try:
      result = self.data_transformer.aggregate_text_features(data)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.aggregate_text_features: {error}'
      self.logger.log_error(error_message, error)


  @io_schema_validation(schema_input=AggregateTextEntity(), schema_output=CleanSentEntity())
  def clean_sentences(self, data: AggregateTextEntity) -> CleanSentEntity:
    try:
      result = self.data_transformer.clean_sentences(data)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.clean_sentences: {error}'
      self.logger.log_error(error_message, error)


  @io_schema_validation(schema_input=CleanSentEntity(), schema_output=RemoveStopsEntity())
  def remove_stopwords(self, data: CleanSentEntity) -> RemoveStopsEntity:
    try:
      result = self.data_transformer.remove_stopwords(data)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.remove_stopwords: {error}'
      self.logger.log_error(error_message, error)
  
  
  @io_schema_validation(schema_input=RemoveStopsEntity(), schema_output=SentEmbeddingEntity())
  def sentence_embedding(self, data: RemoveStopsEntity) -> SentEmbeddingEntity:
    try:
      result = self.data_transformer.generate_sent_embeddings(data)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.generate_sent_embeddings: {error}'
      self.logger.log_error(error_message, error)
  
  
  @io_schema_validation(schema_input=SentEmbeddingEntity(), schema_output=SentPairEntity())
  def sentence_pairing(self, data: SentEmbeddingEntity) -> SentPairEntity:
    try:
      result = self.data_transformer.generate_sent_pairs(data)
      return result
    except Exception as error:
      error_message = f'PreprocessDataUsecase.generate_sent_pairs: {error}'
      self.logger.log_error(error_message, error)