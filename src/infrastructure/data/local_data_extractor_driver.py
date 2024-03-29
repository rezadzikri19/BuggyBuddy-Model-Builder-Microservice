import os
import pandas as pd

from ...core.entities.data.base_data_entity import BaseDataMatrixEntity
from ...core.entities.data.extracted_data_entity import ExtractedDataEntity

from ...core.ports.data.data_extractor_port import DataExtractorPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_wrapper_util import dataframe_wrapper

class LocalDataExtractorDriver(DataExtractorPort):
  def __init__(
      self,
      data_dir_path: str,
      logger: LoggerPort) -> None:
    self.data_dir_path = data_dir_path
    self.logger = logger
  
  
  @dataframe_wrapper
  def get_data_from_source(self, data: None = None) -> BaseDataMatrixEntity:
    try:
      data_dir = os.path.join(self.data_dir_path, 'data', 'extracted_data')
      os.makedirs(data_dir, exist_ok=True)
        
      file_name = 'extracted_data.parquet'
      data_path = os.path.join(data_dir, file_name)
      
      result = pd.read_parquet(data_path)
      return result
    except Exception as error:
      error_message = f'DataExtractorDriver.get_data_from_source: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def get_preprocessed_data(self, data: None = None) -> BaseDataMatrixEntity:
    try:
      data_dir = os.path.join(self.data_dir_path, 'data', 'preprocessed_data')
      os.makedirs(data_dir, exist_ok=True)
              
      file_name = 'preprocessed_data.parquet'
      data_path = os.path.join(data_dir, file_name)
      
      result = pd.read_parquet(data_path)
      return result
    except Exception as error:
      error_message = f'DataExtractorDriver.get_preprocessed_data: {error}'
      self.logger.log_error(error_message, error)
      

  @dataframe_wrapper
  def format_data(self, data: BaseDataMatrixEntity) -> ExtractedDataEntity:
    try:
      return data
    except Exception as error:
      error_message = f'DataExtractorDriver.format_data: {error}'
      self.logger.log_error(error_message, error)