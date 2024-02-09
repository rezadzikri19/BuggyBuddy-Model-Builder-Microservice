import gc
from typing import List

import pandas as pd
from sentence_transformers import SentenceTransformer

from ...core.dtos.data.data_preprocessing_dto import *
from ...core.entities.data.extracted_data_entity import ExtractedDataEntity

from ...core.ports.data.data_preprocessor_port import DataPreprocessorPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_wrapper_util import dataframe_wrapper
from ...infrastructure.utils.common_util import remove_special_chars, remove_stops


class DataPreprocessorDriver(DataPreprocessorPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
  
  
  @dataframe_wrapper
  def drop_features(self, data: ExtractedDataEntity, features_to_drop: List[str]) -> DropFeatsDTO:
    try:
      data = data.drop(columns=features_to_drop, axis=1)
      return data
    except Exception as error:
      error_message = f'DataPreprocessorDriver.drop_features: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def remove_duplicates(self, data: DropFeatsDTO, keep: str = 'first') -> RemoveDuplicatesDTO:
    try:
      columns = list(data.columns)
      data = data.loc[data.astype(str).drop_duplicates(subset=columns, keep=keep).index]
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.remove_duplicates: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def aggregate_text_features(self, data: RemoveDuplicatesDTO) -> AggregateTextDTO:
    try:
      data['text'] = data['platform'] + ' ' + data['summary'] + ' ' + data['description']
      data = data.drop(columns=['platform', 'summary', 'description'], axis=1)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.aggregate_text_features: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def clean_sentences(self, data: AggregateTextDTO) -> CleanSentDTO:
    try:
      data['text_cleaned'] = data['text'].apply(remove_special_chars)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.clean_sentences: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def remove_stopwords(self, data: CleanSentDTO) -> RemoveStopsDTO:
    try:
      data['text_cleaned'] = data['text'].apply(remove_stops)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.remove_stopwords: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def generate_sent_embeddings(self, data: RemoveStopsDTO) -> SentEmbeddingDTO:
    try:
      sent_embd_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
      data['text_embedded'] = data['text_cleaned'].apply(sent_embd_model.encode).tolist()
      data = data.drop(columns=['text_cleaned'])
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.sent_embedding: {error}'
      self.logger.log_error(error_message, error)
      
      
  @dataframe_wrapper
  def generate_sent_pairs(self, data: SentEmbeddingDTO) -> SentPairDTO:
    try:
      # Create duplicated sentence pairs
      df_duplicates = data[data['duplicates_to'] != -1].copy()      
      df_duplicates = pd.merge(
        left=df_duplicates,
        right=df_uniques,
        left_on='duplicates_to',
        right_on='id',
        suffixes=('_left', '_right'))
      df_duplicates = df_duplicates[['duplicates_to_left', 'duplicates_to_right']]
      df_duplicates['label'] = 1
      df_duplicates = df_duplicates.reset_index(drop=True)
      
      # Create unique sentence pairs
      df_uniques = data[data['duplicates_to'] == -1].copy()
      df_uniques = df_uniques.sample(frac=1, replace=False, random_state=42)
      df_uniques_temp = pd.DataFrame()
      df_uniques_temp['text_embedded_left'] = df_uniques['text_embedded']
      df_uniques_temp['text_embedded_right'] = df_uniques['text_embedded'].shift(1)
      df_uniques_temp = df_uniques_temp.dropna()
      df_uniques_temp['label'] = 0
      df_uniques = df_uniques_temp.reset_index(drop=True)

      data = pd.concat([df_duplicates, df_uniques], axis=0)\
        .sample(frac=1, replace=False, random_state=42)\
        .reset_index(drop=True)
      return data
    except Exception as error:
      error_message = f'DataTransformerDriver.sent_embedding: {error}'
      self.logger.log_error(error_message, error)