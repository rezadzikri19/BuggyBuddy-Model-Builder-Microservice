import pandas as pd
from ...core.entities.data.base_data_entity import BaseDataMatrixEntity, BaseDataArrayEntity


def base_matrix_to_dataframe(data_matrix: BaseDataMatrixEntity) -> pd.DataFrame:
  return pd.DataFrame(data=data_matrix.data, columns=data_matrix.columns, index=data_matrix.index)


def base_array_to_series(data_array: BaseDataArrayEntity) -> pd.Series:
  return pd.Series(data=data_array.data, columns=data_array.column, index=data_array.index)


def dataframe_to_base_matrix(df_data: pd.DataFrame) -> BaseDataMatrixEntity:
  return BaseDataMatrixEntity(data=df_data.values.tolist(), columns=list(df_data.columns), index=list(df_data.index))


def series_to_base_array(sr_data: pd.Series) -> BaseDataArrayEntity:
  return pd.Series(data=sr_data.values.tolist(), columns=sr_data.name, index=sr_data.index)


def dataframe_wrapper(func):
  def wrapper(self, data: BaseDataMatrixEntity, *args, **kwargs) -> BaseDataMatrixEntity:
    if data is not None:
      data = base_matrix_to_dataframe(data)
      
    data = func(self, data=data, *args, **kwargs)
    
    if data is not None:
      data = dataframe_to_base_matrix(data)
    return data
  return wrapper


def series_wrapper(func):
  def wrapper(self, data: BaseDataArrayEntity, *args, **kwargs) -> BaseDataArrayEntity:
    if data is not None:
      data = base_array_to_series(data)
      
    data = func(self, data=data, *args, **kwargs)
    
    if data is not None:
      data = series_to_base_array(data)
    return data
  return wrapper