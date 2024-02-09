from typing import TypedDict

from ...entities.model.base_model_entity import BaseModelEntity

class TrainModelsDTO(TypedDict):
    model_training: BaseModelEntity
    model_embedding: BaseModelEntity
    similarity_threshold: float