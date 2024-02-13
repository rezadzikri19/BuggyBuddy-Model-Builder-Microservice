from abc import ABC, abstractmethod

from ....core.entities.data.preprocessed_data_entity import PreprocessedDataEntity

class DataLoaderPort(ABC):
  @abstractmethod
  def dump_preprocessed_data(self, data: PreprocessedDataEntity) -> None:
    pass