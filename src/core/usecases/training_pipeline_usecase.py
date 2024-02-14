from ...core.usecases.model.model_create_usecase import ModelCreateUsecase
from ...core.usecases.model.model_train_usecase import ModelTrainUsecase
from ...core.usecases.model.model_evaluate_usecase import ModelEvaluateUsecase
from ...core.usecases.model.model_save_usecase import ModelSaveUsecase

from ...core.usecases.data.data_extract_usecase import ExtractDataUsecase
from ...core.usecases.data.data_preprocess_usecase import PreprocessDataUsecase
from ...core.usecases.data.data_load_usecase import LoadDataUsecase

from ...core.ports.logger_port import LoggerPort
from ...core.ports.message_broker_port import MessageBrokerPort

class TrainingPipelineUsecase:
  def __init__(
      self,
      model_create_usecase: ModelCreateUsecase,
      model_train_usecase: ModelTrainUsecase,
      model_evaluate_usecase: ModelEvaluateUsecase,
      model_save_usecase: ModelSaveUsecase,
      data_extract_usecase: ExtractDataUsecase,
      data_preprocess_usecase: PreprocessDataUsecase,
      data_load_usecase: LoadDataUsecase,
      message_broker: MessageBrokerPort,
      logger: LoggerPort
      ) -> None:
    self.model_create_usecase = model_create_usecase
    self.model_train_usecase = model_train_usecase
    self.model_evaluate_usecase = model_evaluate_usecase
    self.model_save_usecase = model_save_usecase
    self.data_extract_usecase = data_extract_usecase
    self.data_preprocess_usecase = data_preprocess_usecase
    self.data_load_usecase = data_load_usecase
    self.message_broker = message_broker  
    self.logger = logger
  
  def run_data_pipeline(self) -> None:
    try:
      result = self.data_extract_usecase.fetch_data_from_source(data=None)
      result = self.data_preprocess_usecase.preprocess_data(result)
      self.data_load_usecase.dump_preprocessed_data(result)
      
      self.message_broker.publish_message(
        exchange='train_service',
        route='data_pipeline',
        data={'status': 'SUCCESS', 'message': 'PIPELINE [DATA] - SUCCESS'})
      self.logger.log_info('PIPELINE [DATA] - SUCCESS')
    except Exception as error:
      error_message = f'TrainingPipelineUsecase.run_data_pipeline: {error}'
      
      self.message_broker.publish_message(
        exchange='train_service',
        route='data_pipeline',
        data={'status': 'failed', 'message': f'{error_message}'})
      self.logger.log_error(error_message, error)
  
  
  def run_model_pipeline(self) -> None:
    try:
      data = self.data_extract_usecase.fetch_preprocessed_data(data=None)
      model_training = self.model_create_usecase.create_models()
      
      train_ = self.model_train_usecase.train_models(model_training, data)
      model_training = train_['model_training']
      model_embedding = train_['model_embedding']
      similarity_threshold = train_['similarity_threshold']
      test_data = train_['test_data']
      
      training_metrics, embedding_metrics = self.model_evaluate_usecase.evaluate_models(
        model_training=model_training,
        model_embedding=model_embedding,
        similarity_threshold=similarity_threshold,
        test_data=test_data)
      
      self.model_save_usecase.save_models(
        model_training=model_training,
        model_embedding=model_embedding,
        model_training_metadata=training_metrics,
        model_embedding_metadata=embedding_metrics)
      
      self.message_broker.publish_message(
        exchange='train_service',
        route='model_pipeline',
        data={'status': 'SUCCESS', 'message': 'PIPELINE [MODEL] - SUCCESS'})
      self.logger.log_info('PIPELINE [MODEL] - SUCCESS')
    except Exception as error:
      error_message = f'TrainingPipelineUsecase.run_model_pipeline: {error}'
      
      self.message_broker.publish_message(
        exchange='train_service',
        route='model_pipeline',
        data={'status': 'failed', 'message': f'{error_message}'})
      self.logger.log_error(error_message, error)
    
  
  def run_training_pipeline(self) -> None:
    try:
      self.run_data_pipeline()
      self.run_model_pipeline()
      
      self.message_broker.publish_message(
        exchange='train_service',
        route='all_pipeline',
        data={'status': 'SUCCESS', 'message': 'PIPELINE [ALL] - SUCCESS'})
      self.logger.log_info('PIPELINE [ALL] - SUCCESS')
    except Exception as error:
      error_message = f'TrainingPipelineUsecase.run_training_pipeline: {error}'
      
      self.message_broker.publish_message(
        exchange='train_service',
        route='all_pipeline',
        data={'status': 'failed', 'message': f'{error_message}'})
      self.logger.log_error(error_message, error)