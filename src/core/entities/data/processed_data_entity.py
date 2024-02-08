from typing import List, Optional, Any

from .base_data_entity import BaseDataMatrixEntity


class ProcessedDataEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)

    self.columns = {
        'embedded_text_left': List[int],
        'embedded_text_right': List[int],
        'label': int
      }