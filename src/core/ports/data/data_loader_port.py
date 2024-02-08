from abc import ABC, abstractmethod

from ....core.entities.data.extracted_data_entity import ExtractedDataEntity
from ....core.entities.data.embedded_data_entity import EmbeddedDataEntity

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_extracted_data(self, data: ExtractedDataEntity) -> None:
    pass
  
  @abstractmethod
  def dump_loaded_data(self, data: EmbeddedDataEntity) -> None:
    pass