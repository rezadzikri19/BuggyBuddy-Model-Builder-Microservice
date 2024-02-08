from ...core.entities.base_entity import BaseMatrixEntity


def validate_data(data: BaseMatrixEntity, schema: BaseMatrixEntity) -> None:
  if list(data.columns) != schema.columns:
    Exception('DataValidationUsecase.validate_data: invalid data!')


def io_schema_validation(schema_input: BaseMatrixEntity = None, schema_output: BaseMatrixEntity = None):
  def decorator(func):
    def wrapper(self, data: BaseMatrixEntity, *args, **kwargs) -> BaseMatrixEntity:
        if data is not None and schema_input is not None:
          validate_data(data, schema_input)
        
        data = func(self, data=data, *args, **kwargs)
        
        if data is not None and schema_output is not None:
          validate_data(data, schema_output)
        return data
    return wrapper
  return decorator
    
    