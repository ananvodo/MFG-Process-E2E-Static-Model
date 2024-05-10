import inspect
from typing import Type, Dict, Any, TypeVar

T = TypeVar('T', bound='InstantiatorMixin')

#########################################################################################################
# MIXIN CLASS
#########################################################################################################


class InstantiatorMixin:
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_dictfile(cls: Type[T], data: Dict[str, Any], key: str) -> T:
        """
        Factory method to create an instance of a class from dictionary data using a specific key.
        """
        instance_data = data[key]
        init_params = inspect.signature(cls.__init__).parameters
        missing_params = [
            param for param in init_params if param != 'self' and param not in instance_data
        ]
        if missing_params:
            raise ValueError(
                f"Missing parameters for initializing {cls.__name__}: {', '.join(missing_params)}"
            )
        return cls(**instance_data)
