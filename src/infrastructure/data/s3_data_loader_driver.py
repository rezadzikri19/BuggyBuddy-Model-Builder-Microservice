from datetime import datetime
from io import BytesIO

import boto3
import pyarrow as pa
import pyarrow.parquet as pq

from ...core.entities.data.embedded_data_entity import EmbeddedDataEntity
from ...core.ports.data.data_loader_port import DataLoaderPort
from ...core.ports.logger_port import LoggerPort

from ..utils.data_wrapper_util import dataframe_wrapper

class S3DataLoaderDriver(DataLoaderPort):
  def __init__(
      self,
      aws_access_key_id: str,
      aws_secret_access_key: str,
      region_name: str,
      bucket_name: str,
      logger: LoggerPort) -> None:
    session = boto3.Session(
      aws_access_key_id=aws_access_key_id,
      aws_secret_access_key=aws_secret_access_key,
      region_name=region_name
    )
    self.s3_client = session.client('s3')
    self.bucket_name = bucket_name
    self.logger = logger
    
    
  @dataframe_wrapper
  def dump_embedded_data(self, data: EmbeddedDataEntity) -> None:
    try:
      # file_name = f'/TRAIN/data/embedded/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_embedded_data.parquet'
      file_name = '/TRAIN/data/embedded/embedded_data.parquet'
      buffer = BytesIO()
      
      arrow_table = pa.Table.from_pandas(data)
      pq.write_table(arrow_table, buffer)
      
      self.s3_client.upload_fileobj(buffer, self.bucket_name, file_name)
    except Exception as error:
      error_message = f'DataLoaderDriver.dump_embedded_data: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def dump_preprocessed_data(self, data: EmbeddedDataEntity) -> None:
    try:
      # file_name = f'/TRAIN/data/preprocessed/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_preprocessed_data.parquet'
      file_name = '/TRAIN/data/preprocessed/preprocessed_data.parquet'
      buffer = BytesIO()
      
      arrow_table = pa.Table.from_pandas(data)
      pq.write_table(arrow_table, buffer)
      
      self.s3_client.upload_fileobj(buffer, self.bucket_name, file_name)
    except Exception as error:
      error_message = f'DataLoaderDriver.dump_preprocessed_data: {error}'
      self.logger.log_error(error_message, error)