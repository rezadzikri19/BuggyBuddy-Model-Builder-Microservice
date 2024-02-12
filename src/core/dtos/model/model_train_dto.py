from typing import TypedDict

from ....core.entities.model.base_model_entity import BaseModelEntity
from ....core.entities.data.preprocessed_data_entity import PreprocessedDataEntity

class TrainModelsDTO(TypedDict):
    model_training: BaseModelEntity
    model_embedding: BaseModelEntity
    similarity_threshold: float
    train_data: PreprocessedDataEntity
    test_data: PreprocessedDataEntity