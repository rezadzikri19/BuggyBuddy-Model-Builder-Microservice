import os
from datetime import datetime
from typing import Any, Dict, Optional

import boto3

from ...core.entities.model.base_model_entity import BaseModelEntity
from ...core.ports.model.model_saver_port import ModelSaverPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.model_wrapper_util import base_model_to_keras_model
from ...infrastructure.utils.common_util import save_json

class S3ModelSaverDriver(ModelSaverPort):
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
    
    
  def save_model_training(self, model: BaseModelEntity, metadata: Optional[Dict[str, Any]] = None) -> None:
    try:
      keras_model = base_model_to_keras_model(model)
      curr_dir = os.getcwd()
      data_dir = os.path.join(curr_dir, 'artifacts', 'models', 'training')
        
      if not os.path.exists(data_dir):
        os.makedirs(data_dir)
          
      # model_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_model_training.bin'
      model_name = 'model_training.bin'
      model_local_path = os.path.join(data_dir, model_name)
      keras_model.save(model_local_path)
      
      model_s3_path = f'/TRAIN/models/training/{model_name}'
      self.s3_client.upload_file(model_local_path, self.bucket_name, model_s3_path)
      
      if metadata is not None:
        # metadata_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_metadata_training.json'
        metadata_name = 'metadata_training.json'
        metadata_local_path = os.path.join(data_dir, metadata_name)
        save_json(metadata, metadata_local_path)
        
        metadata_s3_path = f'/TRAIN/models/training/{metadata_name}'
        self.s3_client.upload_file(metadata_local_path, self.bucket_name, metadata_s3_path)
    except Exception as error:
      error_message = f'S3ModelSaverDriver.save_model_training: {error}'
      self.logger.log_error(error_message, error)
    
    
  def save_model_embedding(self, model: BaseModelEntity, metadata: Optional[Dict[str, Any]] = None) -> None:
    try:
      keras_model = base_model_to_keras_model(model)
      curr_dir = os.getcwd()
      data_dir = os.path.join(curr_dir, 'artifacts', 'models', 'embedding')
        
      if not os.path.exists(data_dir):
        os.makedirs(data_dir)
          
      # model_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_model_embedding.bin'
      model_name = 'model_embedding.bin'
      model_local_path = os.path.join(data_dir, model_name)
      keras_model.save(model_local_path)
      
      model_s3_path = f'/TRAIN/models/embedding/{model_name}'
      self.s3_client.upload_file(model_local_path, self.bucket_name, model_s3_path)
      
      if metadata is not None:
        # metadata_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_metadata_embedding.json'
        metadata_name = 'metadata_embedding.json'
        metadata_local_path = os.path.join(data_dir, metadata_name)
        save_json(metadata, metadata_local_path)
        
        metadata_s3_path = f'/TRAIN/models/embedding/{metadata_name}'
        self.s3_client.upload_file(metadata_local_path, self.bucket_name, metadata_s3_path)
    except Exception as error:
      error_message = f'S3ModelSaverDriver.save_model_embedding: {error}'
      self.logger.log_error(error_message, error)