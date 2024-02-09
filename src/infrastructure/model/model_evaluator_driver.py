from ...core.dtos.model.model_evaluate_dto import ModelMetricsDTO

from ...core.entities.data.preprocessed_data_entity import PreprocessedDataEntity
from ...core.entities.model.base_model_entity import BaseModelEntity
from ...core.ports.model.model_evaluator_port import ModelEvaluatorPort
from ...core.ports.logger_port import LoggerPort

from ...infrastructure.utils.data_wrapper_util import base_matrix_to_dataframe
from ...infrastructure.utils.model_wrapper_util import base_model_to_keras_model
from ...infrastructure.utils.common_util import custom_cosine_similarity, evaluate_embedding_model

import numpy as np
from sklearn.metrics import precision_score, recall_score, roc_auc_score

class ModelEvaluatorDriver(ModelEvaluatorPort):
  def __init__(self, logger: LoggerPort) -> None:
    self.logger = logger
  
  
  def evaluate_model_training(self, model: BaseModelEntity, test_data: PreprocessedDataEntity) -> ModelMetricsDTO:
    df_test_data = base_matrix_to_dataframe(test_data)
    keras_model = base_model_to_keras_model(model)
    
    X_test, y_test = df_test_data.drop(columns=['label']), df_test_data['label']
    X_test_inputs = [np.vstack(X_test['text_embedded_left']), np.vstack(X_test['text_embedded_right'])]
    
    y_pred = keras_model.predict(X_test_inputs)
    
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)
    
    return {
        'precision': precision,      
        'recall': recall,
        'roc_auc': roc_auc      
      }
    
  
  def evaluate_model_embedding(self, model: BaseModelEntity, test_data: PreprocessedDataEntity, threshold: float) -> ModelMetricsDTO:
    df_test_data = base_matrix_to_dataframe(test_data)
    keras_model = base_model_to_keras_model(model)

    embd_test_left = keras_model.predict(np.vstack(df_test_data['text_embedded_left']))
    embd_test_right = keras_model.predict(np.vstack(df_test_data['text_embedded_right']))
    similarity_scores = np.array([custom_cosine_similarity(embd_1, embd_2) for embd_1, embd_2 in zip(embd_test_left, embd_test_right)])
    
    precision, recall, roc_auc = evaluate_embedding_model(similarity_scores, df_test_data['label'], threshold)
    return {
        'precision': precision,
        'recall': recall,
        'roc_auc': roc_auc
      }