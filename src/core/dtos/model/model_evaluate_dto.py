from typing import TypedDict

class ModelMetricsDTO(TypedDict):
    precision: float
    recall: float
    roc_auc: float