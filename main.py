from src.core.usecases.data.data_extract_usecase import ExtractDataUsecase
from src.core.usecases.data.data_preprocess_usecase import PreprocessDataUsecase
from src.core.usecases.data.data_load_usecase import LoadDataUsecase
from src.core.usecases.model.model_create_usecase import ModelCreateUsecase
from src.core.usecases.model.model_train_usecase import ModelTrainUsecase
from src.core.usecases.model.model_evaluate_usecase import ModelEvaluateUsecase
from src.core.usecases.model.model_save_usecase import ModelSaveUsecase
from src.core.usecases.training_pipeline_usecase import TrainingPipelineUsecase

from src.infrastructure.data.data_extractor_driver import DataExtractorDriver
from src.infrastructure.data.data_preprocessor_driver import DataPreprocessorDriver
from src.infrastructure.data.data_loader_driver import DataLoaderDriver
from src.infrastructure.model.model_creator_driver import ModelCreatorDriver
from src.infrastructure.model.model_trainer_driver import ModelTrainerDriver
from src.infrastructure.model.model_evaluator_driver import ModelEvaluatorDriver
from src.infrastructure.model.model_saver_driver import ModelSaverDriver
from src.infrastructure.loggers.logger_driver import LoggerDriver

def main():
  logger_driver = LoggerDriver()
  
  data_extractor_driver = DataExtractorDriver(logger_driver)
  data_preprocessor_driver = DataPreprocessorDriver(logger_driver)
  data_loader_driver = DataLoaderDriver(logger_driver)
  
  model_creator_driver = ModelCreatorDriver(logger_driver)
  model_trainer_driver = ModelTrainerDriver(logger_driver)
  model_evaluator_driver = ModelEvaluatorDriver(logger_driver)
  model_saver_driver = ModelSaverDriver(logger_driver)
  
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
    logger=logger_driver)
  
  result = training_pipeline_usecase.run_data_pipeline()
  # training_pipeline_usecase.run_model_pipeline(result)
  # training_pipeline_usecase.run_training_pipeline()

if __name__ == "__main__":
  main()