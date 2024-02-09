from abc import ABC, abstractmethod
from typing import List

from ....core.entities.data.extracted_data_entity import ExtractedDataEntity
from ....core.dtos.data.data_preprocessing_dto import *

class DataPreprocessorPort(ABC):
  @abstractmethod
  def drop_features(self, data: ExtractedDataEntity, features_to_drop: List[str]) -> DropFeatsEntity:
    pass
  
  @abstractmethod
  def remove_duplicates(self, data: DropFeatsEntity, keep: str = 'first') -> RemoveDuplicatesEntity:
    pass
  
  @abstractmethod
  def aggregate_text_features(self, data: RemoveDuplicatesEntity) -> AggregateTextEntity:
    pass
  
  @abstractmethod
  def clean_sentences(self, data: AggregateTextEntity) -> CleanSentEntity:
    pass
  
  @abstractmethod
  def remove_stopwords(self, data: CleanSentEntity) -> RemoveStopsEntity:
    pass
  
  @abstractmethod
  def generate_sent_embeddings(self, data: RemoveStopsEntity) -> SentEmbeddingEntity:
    pass
  
  @abstractmethod
  def generate_sent_pairs(self, data: SentEmbeddingEntity) -> SentPairEntity:
    pass