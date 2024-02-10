from typing import List, Optional, Any

from .base_data_entity import BaseDataMatrixEntity

class PreprocessedDataEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'text_embedded_left': List[float],
        'text_embedded_right': List[float],
        'label': int
      }