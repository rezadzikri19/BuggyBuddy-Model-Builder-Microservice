from abc import ABC, abstractmethod
from typing import List

from ....core.entities.data.extracted_data_entity import ExtractedDataEntity
from ....core.dtos.data.data_preprocessing_dto import *

class DataPreprocessorPort(ABC):
  @abstractmethod
  def drop_features(self, data: ExtractedDataEntity, features_to_drop: List[str]) -> DropFeatsDTO:
    pass
  
  @abstractmethod
  def remove_duplicates(self, data: DropFeatsDTO, keep: str = 'first') -> RemoveDuplicatesDTO:
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: RemoveDuplicatesDTO) -> AggregateTextDTO:
    pass
  
  @abstractmethod
  def clean_sentences(self, data: AggregateTextDTO) -> CleanSentDTO:
    pass
  
  @abstractmethod
  def remove_stopwords(self, data: CleanSentDTO) -> RemoveStopsDTO:
    pass
  
  @abstractmethod
  def generate_sent_embeddings(self, data: RemoveStopsDTO) -> SentEmbeddingDTO:
    pass
  
  @abstractmethod
  def generate_sent_pairs(self, data: SentEmbeddingDTO) -> SentPairDTO:
    pass