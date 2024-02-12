from typing import Any, List
from ..data.base_data_entity import BaseDataMatrixEntity, BaseDataArrayEntity

class BaseModelEntity:
  def __init__(self, model: Any) -> None:
    self.model = model   
    self._validate()
      
    
  def _validate(self):
    if not hasattr(self.model, 'fit') and callable(getattr(self, 'fit')):
      raise Exception('model should has "fit" method')
    
    if not hasattr(self.model, 'evaluate') and callable(getattr(self, 'evaluate')):
      raise Exception('model should has "evaluate" method')
    
    if not hasattr(self.model, 'predict') and callable(getattr(self, 'predict')):
      raise Exception('model should has "predict" method')
  
  
  def fit(self, X: BaseDataMatrixEntity, y: BaseDataArrayEntity) -> None:
    self.model.fit(X, y)
    
    
  def evaluate(self, X: BaseDataMatrixEntity, y: BaseDataArrayEntity) -> List[float]:
    return self.model.evaluate(X, y)
    
    
  def predict(self, X: BaseDataMatrixEntity, y: None = None) -> BaseDataArrayEntity:
    return self.model.predict(X, y)