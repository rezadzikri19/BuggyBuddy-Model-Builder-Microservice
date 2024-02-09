from ...core.usecases.model.model_create_usecase import ModelCreateUsecase
from ...core.usecases.model.model_train_usecase import ModelTrainUsecase
from ...core.usecases.model.model_evaluate_usecase import ModelEvaluateUsecase
from ...core.usecases.model.model_save_usecase import ModelSaveUsecase

from ...core.usecases.data.data_extract_usecase import ExtractDataUsecase
from ...core.usecases.data.data_preprocess_usecase import PreprocessDataUsecase
from ...core.usecases.data.data_load_usecase import LoadDataUsecase

from ...core.entities.data.processed_data_entity import ProcessedDataEntity

class TrainingPipeline:
  def __init__(
      self,
      model_create_usecase: ModelCreateUsecase,
      model_train_usecase: ModelTrainUsecase,
      model_evaluate_usecase: ModelEvaluateUsecase,
      model_save_usecase: ModelSaveUsecase,
      data_extract_usecase: ExtractDataUsecase,
      data_preprocess_usecase: PreprocessDataUsecase,
      data_load_usecase: LoadDataUsecase,
      ) -> None:
    self.model_create_usecase = model_create_usecase
    self.model_train_usecase = model_train_usecase
    self.model_evaluate_usecase = model_evaluate_usecase
    self.model_save_usecase = model_save_usecase
    self.data_extract_usecase = data_extract_usecase
    self.data_preprocess_usecase = data_preprocess_usecase
    self.data_load_usecase = data_load_usecase
    
  
  def run_data_pipeline(self):
    result = self.data_extract_usecase.fetch_data()
    result = self.data_preprocess_usecase.preprocess_data(result)
    self.data_load_usecase.dump_preprocessed_data(result)
    return result
  
  
  def run_model_pipeline(self, data: ProcessedDataEntity):
    model_training = self.model_create_usecase.create_models()
    
    train_ = self.model_train_usecase.train_models(model_training, data)
    model_training = train_['model_training']
    model_embedding = train_['model_embedding']
    similarity_threshold = train_['similarity_threshold']
    
    training_metrics, embedding_metrics = self.model_evaluate_usecase.evaluate_models(
      model_training=model_training,
      model_embedding=model_embedding,
      similarity_threshold=similarity_threshold)
    
    self.model_save_usecase.save_models(
      model_training=model_training,
      model_embedding=model_embedding,
      model_training_metadata=training_metrics,
      model_embedding_metadata=embedding_metrics)