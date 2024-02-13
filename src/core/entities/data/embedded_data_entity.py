from typing import Any, List, Optional

from .base_data_entity import BaseDataMatrixEntity

class EmbeddedDataEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'id': int,
        'type': str,
        'product': str,
        'component': str,
        'platform': str,
        'summary': str,
        'description': str,
        'vector': List[int],
      }