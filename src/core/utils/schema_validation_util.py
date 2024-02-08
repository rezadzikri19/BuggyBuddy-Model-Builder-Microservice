from ..entities.data.base_data_entity import BaseDataMatrixEntity


def validate_data(data: BaseDataMatrixEntity, schema: BaseDataMatrixEntity) -> None:
  if list(data.columns) != schema.columns:
    Exception('DataValidationUsecase.validate_data: invalid data!')


def io_schema_validation(schema_input: BaseDataMatrixEntity = None, schema_output: BaseDataMatrixEntity = None):
  def decorator(func):
    def wrapper(self, data: BaseDataMatrixEntity, *args, **kwargs) -> BaseDataMatrixEntity:
        if data is not None and schema_input is not None:
          validate_data(data, schema_input)
        
        data = func(self, data=data, *args, **kwargs)
        
        if data is not None and schema_output is not None:
          validate_data(data, schema_output)
        return data
    return wrapper
  return decorator
    
    