from typing import List, Optional, Any

from .base_data_entity import BaseDataMatrixEntity


class DropFeatsEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'bug_id': int,
        'platform': str,
        'summary': str,
        'description': str,
        'duplicates_to': int
      }



class RemoveDuplicatesEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'platform': str,
        'summary': str,
        'description': str,
        'duplicates_to': int
      }
    


class AggregateTextEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'duplicates_to': int
      }



class CleanSentEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'text_cleaned': str,
        'duplicates_to': int
      }



class RemoveStopsEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'text_cleaned': str,
        'duplicates_to': int
      }



class SentEmbeddingEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'text': str,
        'embedded_text': List[int],
        'duplicates_to': int
      }



class SentPairEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'bug_id': int,
        'embedded_text_left': List[int],
        'embedded_text_right': List[int],
        'label': int
      }