from typing import Optional, Tuple

from core.entities.model.base_model_entity import BaseModelEntity

from ...core.entities.data.processed_data_entity import ProcessedDataEntity
from ...core.ports.model.model_trainer_port import ModelTrainer
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.common_util import custom_cosine_similarity, evaluate_embedding_model

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from keras.callbacks import EarlyStopping

class ModelTrainerDriver(ModelTrainer):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
    
  
  def split_train_test_data(self, data: ProcessedDataEntity, test_ratio: int = 0.2) -> Tuple(ProcessedDataEntity, ProcessedDataEntity):
    data_train, data_test = train_test_split(
      data,
      shuffle=True,
      stratify=data['label'],
      test_size=test_ratio,
      random_state=42)
    return (data_train, data_test)
  
  
  def train_model_training(self, model: BaseModelEntity, train_data: ProcessedDataEntity, valid_data: Optional[ProcessedDataEntity] = None) -> None:
    early_stopping = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)
    
    X_train, y_train = train_data.drop(columns=['label']), train_data['label']
    X_valid, y_valid = valid_data.drop(columns=['label']), valid_data['label']
    
    X_train_inputs = [np.vstack(X_train['text_embedded_left']), np.vstack(X_train['text_embedded_right'])]
    X_valid_inputs = [np.vstack(X_valid['text_embedded_left']), np.vstack(X_valid['text_embedded_right'])]
        
    epochs, batch_size = 10, 32
    
    model.fit(
      X_train_inputs, y_train,
      epochs=epochs,
      batch_size=batch_size,
      validation_data=(X_valid_inputs, y_valid),
      callbacks=[early_stopping],
      verbose=0)
    
  
  def get_similarity_threshold(self, model: BaseModelEntity, data: ProcessedDataEntity) -> float:
    thresholds = np.linspace(0, 1, 1000)
    
    embd_test_left = model.predict(np.vstack(data['text_embedded_left']))
    embd_test_right = model.predict(np.vstack(data['text_embedded_right']))
    similarity_scores = np.array([custom_cosine_similarity(embd_1, embd_2) for embd_1, embd_2 in zip(embd_test_left, embd_test_right)])
    
    threshold_eval = pd.DataFrame([[threshold, *evaluate_embedding_model(similarity_scores, threshold)] for threshold in thresholds], columns=['threshold', 'precision', 'recall', 'auc'])
    max_threshold = threshold_eval.loc[threshold_eval['auc'].argmax()]
    
    return max_threshold