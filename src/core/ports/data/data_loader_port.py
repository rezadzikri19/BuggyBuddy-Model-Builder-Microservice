from abc import ABC, abstractmethod

from ....core.entities.data.embedded_data_entity import EmbeddedDataEntity
from ....core.entities.data.preprocessed_data_entity import PreprocessedDataEntity

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_preprocessed_data(self, data: PreprocessedDataEntity) -> None:
    pass
  
  @abstractmethod
  def dump_embedded_data(self, data: EmbeddedDataEntity) -> None:
    pass