from abc import ABC, abstractmethod

from process_params.Params import T

#########################################################################################################
# ABSTRACT CLASS
#########################################################################################################


class Equipment(ABC):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    @abstractmethod
    def from_params(cls, *args, **kwargs) -> None:
        '''
        Implement in subclass with required parameters.
        '''
        pass

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def load_params(self, params: T) -> None:
        '''
        Load parameters from a params object from Params class or subclasses to a equipment object.
        '''
        # Loop through attributes of the instance params object and set them to self
        for attr_name, attr_value in vars(params).items():
            # Set each attribute to self only if it does not exist in self
            if not hasattr(self, attr_name):
                setattr(self, attr_name, attr_value)
