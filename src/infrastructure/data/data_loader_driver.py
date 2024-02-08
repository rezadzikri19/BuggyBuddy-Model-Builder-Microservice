import os
import datetime

from ...core.entities.data.embedded_data_entity import EmbeddedDataEntity

from ...core.ports.data.data_loader_port import DataLoaderPort
from ...core.ports.logger_port import LoggerPort

class DataLoaderDriver(DataLoaderPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
    
    
  def dump_embedded_data(self, data: EmbeddedDataEntity) -> None:
    try:
      curr_dir = os.getcwd()
      data_dir = os.path.join(curr_dir, 'artifacts', 'embedded_data')
      
      if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
      file_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_embedded_data.parquet'
      
      data_path = os.path.join(data_dir, file_name)  
      data.to_parquet(data_path)
    except Exception as error:
      error_message = f'DataLoaderDriver.dump_embedded_data: {error}'
      self.logger.log_error(error_message, error)