from abc import ABC, abstractmethod

from ....core.entities.data.extracted_data_entity import ExtractedDataEntity

class DataExtractorPort(ABC):
  @abstractmethod
  def get_data_from_source(self, data: None = None) -> ExtractedDataEntity:
    pass