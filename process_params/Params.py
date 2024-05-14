import inspect
from typing import Type, TypeVar

T = TypeVar('T', bound='Params')
#########################################################################################################
# CLASS
#########################################################################################################


class Params:
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_dictfile(cls: Type[T], data: dict[str, any], key: str) -> T:

        if key not in data:
            raise KeyError(
                f"Key '{key}' not found in provided data dictionary.")

        instance_data = data[key]
        init_params = inspect.signature(cls.__init__).parameters
        missing_params = [
            param for param in init_params if param != 'self' and param not in instance_data
        ]

        if missing_params:
            raise ValueError(
                f"Missing parameters for initializing {cls.__name__}: {', '.join(missing_params)}")

        return cls(**instance_data)
