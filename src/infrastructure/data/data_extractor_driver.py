import os
import pandas as pd

from ...core.entities.data.base_data_entity import BaseDataMatrixEntity
from ...core.entities.data.extracted_data_entity import ExtractedDataEntity

from ...core.ports.data.data_extractor_port import DataExtractorPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_wrapper_util import dataframe_wrapper

class DataExtractorDriver(DataExtractorPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
  
  
  @dataframe_wrapper
  def get_data_from_source(self, data: None = None) -> BaseDataMatrixEntity:
    try:
      curr_dir = os.getcwd()
      data_dir = os.path.join(curr_dir, 'artifacts', 'extracted_data')
      
      if not os.path.exists(data_dir):
          os.makedirs(data_dir)
          
          raise Exception('directory not found!')
        
      file_name = 'extracted_data.parquet'
      data_path = os.path.join(data_dir, file_name)
      
      result = pd.read_parquet(data_path)
      return result
    except Exception as error:
      error_message = f'DataExtractorDriver.get_data_from_source: {error}'
      self.logger.log_error(error_message, error)
      

  @dataframe_wrapper
  def format_data(self, data: BaseDataMatrixEntity) -> ExtractedDataEntity:
    try:
      return data
    except Exception as error:
      error_message = f'DataExtractorDriver.format_data: {error}'
      self.logger.log_error(error_message, error)