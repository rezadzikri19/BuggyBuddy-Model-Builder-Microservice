from typing import Tuple

from ....core.ports.model.model_creator_port import ModelCreatorPort
from ....core.entities.model.base_model_entity import BaseModelEntity

class ModelCreateUsecase:
  def __init__(self, model_creator: ModelCreatorPort) -> None:
    self.model_creator = model_creator
  
  
  def create_models(self) -> Tuple[BaseModelEntity]:
    model_training = self.model_creator.create_model_training()
    model_embedding = self.model_creator.create_model_embedding(model_training)
    
    return (model_training, model_embedding)