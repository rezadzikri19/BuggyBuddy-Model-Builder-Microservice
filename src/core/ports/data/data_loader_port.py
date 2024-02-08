from abc import ABC, abstractmethod

from ....core.entities.data.embedded_data_entity import EmbeddedDataEntity

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_embedded_data(self, data: EmbeddedDataEntity) -> None:
    pass