from typing import List, Optional, Any, Dict


class BaseDataMatrixEntity:
  def __init__(
      self,
      columns: Optional[Dict[str, Any]] = None,
      data: Optional[List[List[Any]]] = None,
      index: Optional[List[Any]] = None) -> None:
    self.columns = columns
    self.data = data
    self.index = index
    self.size = None
    
    self._validate_size()
    self._validate_types()
    
    if index is None and data is not None:
      self.index = list(range(len(data)))
  
  
  def _validate_size(self) -> None:
    if self.data is None:
      return

    result = all(len(row) == len(self.data[0]) for row in self.data)
    
    if not result:
      raise Exception('BaseMatrixEntity._validate_size: incorrect matrix size!')
    
    if self.columns is not None and len(self.data[0]) != len(self.columns):
      raise Exception('BaseMatrixEntity._validate_size: data size does not match with number of columns!')
    
    self.size = (len(self.data), len(self.columns))
  
  
  def _validate_types(self) -> None:
    if self.data is None:
      return

    transposed = list(map(list, zip(*self.data)))
    transposed = [sorted(col, key=lambda item: 1 if item is None else 0) for col in transposed]
    
    result = all(all((type(item) == type(row[0])) or (item is None) for item in row) for row in transposed)
    
    if not result:
      raise Exception('BaseMatrixEntity._validate_types: mixing data type found!')

  
  def __getitem__(self, key):
    if type(key) == list:
      idx, col = key
      col_idx = self.columns.index(col)
      return self.data[idx][col_idx]
    
    return self.data[key]



class BaseDataArrayEntity:
  def __init__(
      self,
      column: Optional[Dict[str, Any]] = None,
      data: Optional[List[Any]] = None,
      index: Optional[List[Any]] = None) -> None:
    self.column = column
    self.data = data
    self.index = index
    self.size = None
    
    self._validate_size()
    self._validate_type()
    
    if index is None and data is not None:
      self.index = list(range(len(data)))
  
  
  def _validate_size(self) -> None:
    if self.data is None:
      return
    
    self.size = (len(self.data), )
  
  
  def _validate_type(self, data: List[Any]) -> None:
    if self.data is None:
      return
    
    result = all(type(item) == type(data[0]) for item in data)
    
    if not result:
      raise Exception('BaseArrayModel._validate_type: mixing data type found!')
  
  
  def __getitem__(self, idx):
    return self.data[idx]