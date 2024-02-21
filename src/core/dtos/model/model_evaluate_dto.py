from typing import TypedDict

class ModelMetricsDTO(TypedDict):
    precision: float
    recall: float
    f1: float