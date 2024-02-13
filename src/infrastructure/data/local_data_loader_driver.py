import os
from datetime import datetime

from ...core.entities.data.preprocessed_data_entity import PreprocessedDataEntity
from ...core.ports.data.data_loader_port import DataLoaderPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_wrapper_util import dataframe_wrapper

class LocalDataLoaderDriver(DataLoaderPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
      
  
  @dataframe_wrapper
  def dump_preprocessed_data(self, data: PreprocessedDataEntity) -> None:
    try:
      curr_dir = os.getcwd()
      data_dir = os.path.join(curr_dir, 'artifacts', 'data', 'preprocessed_data')
      
      if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
      # file_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_preprocessed_data.parquet'
      file_name = 'preprocessed_data.parquet'
      
      data_path = os.path.join(data_dir, file_name)  
      data.to_parquet(data_path)
    except Exception as error:
      error_message = f'DataLoaderDriver.dump_preprocessed_data: {error}'
      self.logger.log_error(error_message, error)