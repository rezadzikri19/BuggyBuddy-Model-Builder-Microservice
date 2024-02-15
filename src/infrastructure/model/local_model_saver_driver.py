from typing import Any, Dict, Optional

from ...core.entities.model.base_model_entity import BaseModelEntity
from ...core.ports.model.model_saver_port import ModelSaverPort
from ...core.ports.logger_port import LoggerPort

from ..utils.model_wrapper_util import base_model_to_keras_model
from ..utils.common_util import save_json

import os
from datetime import datetime

class LocalModelSaverDriver(ModelSaverPort):
  def __init__(
      self,
      data_dir_path: str,
      logger: LoggerPort) -> None:
    self.data_dir_path = data_dir_path
    self.logger = logger
    
    
  def save_model_training(self, model: BaseModelEntity, metadata: Optional[Dict[str, Any]] = None) -> None:
    try:
      keras_model = base_model_to_keras_model(model)
      data_dir = os.path.join(self.data_dir_path, 'models', 'training')
      os.makedirs(data_dir, exist_ok=True)
                  
      # model_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_model_training.h5'
      model_name = 'model_training.h5'
      model_path = os.path.join(data_dir, model_name)
      keras_model.save(model_path)
      
      if metadata is not None:
        # metadata_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_metadata_training.json'
        metadata_name = 'metadata_training.json'
        metadata_path = os.path.join(data_dir, metadata_name)
        save_json(metadata, metadata_path)
    except Exception as error:
      error_message = f'LocalModelSaverDriver.save_model_training: {error}'
      self.logger.log_error(error_message, error)
    
    
  def save_model_embedding(self, model: BaseModelEntity, metadata: Optional[Dict[str, Any]] = None) -> None:
    try:
      keras_model = base_model_to_keras_model(model)
      data_dir = os.path.join(self.data_dir_path, 'models', 'embedding')
      os.makedirs(data_dir, exist_ok=True)
                  
      # model_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_model_embedding.h5'
      model_name = 'model_embedding.h5'
      model_path = os.path.join(data_dir, model_name)
      keras_model.save(model_path)
      
      if metadata is not None:
        # metadata_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_metadata_embedding.json'
        metadata_name = 'metadata_embedding.json'
        metadata_path = os.path.join(data_dir, metadata_name)
        save_json(metadata, metadata_path)
    except Exception as error:
      error_message = f'LocalModelSaverDriver.save_model_embedding: {error}'
      self.logger.log_error(error_message, error)