from typing import TypedDict

from ....core.entities.model.base_model_entity import BaseModelEntity


class ModelMetricsDTO(TypedDict):
    precision: float
    recall: float
    roc_auc: float