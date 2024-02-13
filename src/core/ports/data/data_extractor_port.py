from abc import ABC, abstractmethod

from ....core.entities.data.base_data_entity import BaseDataMatrixEntity
from ....core.entities.data.extracted_data_entity import ExtractedDataEntity

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, data: None = None) -> BaseDataMatrixEntity:
    pass
  
  @abstractmethod
  def get_preprocessed_data(self, data: None = None) -> BaseDataMatrixEntity:
    pass
  
  @abstractmethod
  def format_data(self, data: BaseDataMatrixEntity) -> ExtractedDataEntity:
    pass