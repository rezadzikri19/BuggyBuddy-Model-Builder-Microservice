from io import BytesIO

import boto3
import pandas as pd

from ...core.entities.data.base_data_entity import BaseDataMatrixEntity
from ...core.entities.data.extracted_data_entity import ExtractedDataEntity

from ...core.ports.data.data_extractor_port import DataExtractorPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_wrapper_util import dataframe_wrapper

class S3DataExtractorDriver(DataExtractorPort):
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
  def get_data_from_source(self, data: None = None) -> BaseDataMatrixEntity:
    try:       
      file_name = 'ETL/data/processed/processed_data.parquet'
      
      response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
      data = response['Body'].read()
    
      result = pd.read_parquet(BytesIO(data))
      return result
    except Exception as error:
      error_message = f'S3DataExtractorDriver.get_data_from_source: {error}'
      self.logger.log_error(error_message, error)
      
  
  @dataframe_wrapper
  def get_preprocessed_data(self, data: None = None) -> BaseDataMatrixEntity:
    try:
      file_name = 'TRAIN/data/preprocessed/preprocessed_data.parquet'

      response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
      data = response['Body'].read()
    
      result = pd.read_parquet(BytesIO(data))
      return result
    except Exception as error:
      error_message = f'S3DataExtractorDriver.get_preprocessed_data: {error}'
      self.logger.log_error(error_message, error)
      

  @dataframe_wrapper
  def format_data(self, data: BaseDataMatrixEntity) -> ExtractedDataEntity:
    try:
      return data
    except Exception as error:
      error_message = f'S3DataExtractorDriver.format_data: {error}'
      self.logger.log_error(error_message, error)