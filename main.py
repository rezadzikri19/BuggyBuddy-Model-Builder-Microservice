import os
from dotenv import load_dotenv

from src.core.usecases.data.data_extract_usecase import ExtractDataUsecase
from src.core.usecases.data.data_preprocess_usecase import PreprocessDataUsecase
from src.core.usecases.data.data_load_usecase import LoadDataUsecase

from src.core.usecases.model.model_create_usecase import ModelCreateUsecase
from src.core.usecases.model.model_train_usecase import ModelTrainUsecase
from src.core.usecases.model.model_evaluate_usecase import ModelEvaluateUsecase
from src.core.usecases.model.model_save_usecase import ModelSaveUsecase

from src.core.usecases.training_pipeline_usecase import TrainingPipelineUsecase

from src.infrastructure.data.local_data_extractor_driver import LocalDataExtractorDriver
from src.infrastructure.data.s3_data_extractor_driver import S3DataExtractorDriver
from src.infrastructure.data.data_preprocessor_driver import DataPreprocessorDriver
from src.infrastructure.data.local_data_loader_driver import LocalDataLoaderDriver
from src.infrastructure.data.s3_data_loader_driver import S3DataLoaderDriver

from src.infrastructure.model.model_creator_driver import ModelCreatorDriver
from src.infrastructure.model.model_trainer_driver import ModelTrainerDriver
from src.infrastructure.model.model_evaluator_driver import ModelEvaluatorDriver
from src.infrastructure.model.local_model_saver_driver import LocalModelSaverDriver
from src.infrastructure.model.s3_model_saver_driver import S3ModelSaverDriver

from src.infrastructure.loggers.logger_driver import LoggerDriver
from src.infrastructure.message.rabbitmq_message_broker_driver import RabbitMQMessageBrokerDriver

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')
BUCKET_NAME = os.getenv('BUCKET_NAME')

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')

logger_driver = LoggerDriver()
message_broker_driver = RabbitMQMessageBrokerDriver(host=RABBITMQ_HOST)

def callback(data):
  logger_driver.log_info(f'message_received: status={data['status']}, message={data['message']}')
  
  if data['status'] != 'done':
    return
    
  data_extractor_driver = S3DataExtractorDriver(
      aws_access_key_id=AWS_ACCESS_KEY_ID,
      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
      region_name=REGION_NAME,
      bucket_name=BUCKET_NAME,
      logger=logger_driver
    )
  data_preprocessor_driver = DataPreprocessorDriver(logger_driver)
  # data_loader_driver = LocalDataLoaderDriver(logger_driver)
  data_loader_driver = S3DataLoaderDriver(
      aws_access_key_id=AWS_ACCESS_KEY_ID,
      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
      region_name=REGION_NAME,
      bucket_name=BUCKET_NAME,
      logger=logger_driver
    )
  
  model_creator_driver = ModelCreatorDriver(logger_driver)
  model_trainer_driver = ModelTrainerDriver(logger_driver)
  model_evaluator_driver = ModelEvaluatorDriver(logger_driver)
  # model_saver_driver = LocalModelSaverDriver(logger_driver)
  model_saver_driver = S3ModelSaverDriver(
      aws_access_key_id=AWS_ACCESS_KEY_ID,
      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
      region_name=REGION_NAME,
      bucket_name=BUCKET_NAME,
      logger=logger_driver
    )
  
  data_extract_usecase = ExtractDataUsecase(data_extractor_driver, logger_driver)
  data_preprocess_usecase = PreprocessDataUsecase(data_preprocessor_driver, logger_driver)
  data_load_usecase = LoadDataUsecase(data_loader_driver, logger_driver)

  model_create_usecase = ModelCreateUsecase(model_creator_driver, logger_driver)
  model_train_usecase = ModelTrainUsecase(model_trainer=model_trainer_driver,
    model_evaluator=model_evaluator_driver,
    model_creator=model_creator_driver,
    logger=logger_driver)
  model_evaluate_usecase = ModelEvaluateUsecase(model_evaluator_driver, logger_driver)
  model_save_usecase = ModelSaveUsecase(model_saver_driver, logger_driver)
  
  training_pipeline_usecase = TrainingPipelineUsecase(
    data_extract_usecase=data_extract_usecase,
    data_preprocess_usecase=data_preprocess_usecase,
    data_load_usecase=data_load_usecase,
    model_create_usecase=model_create_usecase,
    model_train_usecase=model_train_usecase,
    model_evaluate_usecase=model_evaluate_usecase,
    model_save_usecase=model_save_usecase,
    message_broker=message_broker_driver,
    logger=logger_driver)
  
  training_pipeline_usecase.run_training_pipeline()


def main():
  message_broker_driver.subscribe_topic(exchange='etl_service', route='all_pipeline', callback=callback)


if __name__ == "__main__":
  main()