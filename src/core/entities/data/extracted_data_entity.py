from typing import Any, List, Optional

from .base_data_entity import BaseDataMatrixEntity

class ExtractedDataEntity(BaseDataMatrixEntity):
  def __init__(self, data: Optional[List[List[Any]]] = None, index: Optional[List[Any]] = None) -> None:
    super().__init__(data=data, index=index)
    
    self.columns = {
        'bug_id': int,
        'report_type': str,
        'status': str,
        'product': str,
        'component': str,
        'platform': str,
        'summary': str,
        'description': str,
        'resolution': str,
        'severity': str,
        'priority': str,
        'duplicates_to': int
      }