from abc import ABC, abstractmethod

from ....core.entities.data.embedded_data_entity import EmbeddedDataEntity
from ....core.entities.data.processed_data_entity import ProcessedDataEntity

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_preprocessed_data(self, data: ProcessedDataEntity) -> None:
    pass
  
  @abstractmethod
  def dump_embedded_data(self, data: EmbeddedDataEntity) -> None:
    pass