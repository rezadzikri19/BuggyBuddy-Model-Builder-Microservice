from typing import List, Optional, Any

from ....core.entities.data.base_data_entity import BaseDataMatrixEntity

class DropFeatsDTO(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'platform': str,
        'summary': str,
        'description': str,
        'duplicates_to': int
      }


class RemoveDuplicatesDTO(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'platform': str,
        'summary': str,
        'description': str,
        'duplicates_to': int
      }
    
    
class AggregateTextDTO(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'text': str,
        'duplicates_to': int
      }


class CleanSentDTO(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'text': str,
        'text_cleaned': str,
        'duplicates_to': int
      }


class RemoveStopsDTO(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'text': str,
        'text_cleaned': str,
        'duplicates_to': int
      }


class SentEmbeddingDTO(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'text': str,
        'text_embedded': List[float],
        'duplicates_to': int
      }


class SentPairDTO(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'text_embedded_left': List[float],
        'text_embedded_right': List[float],
        'label': int
      }