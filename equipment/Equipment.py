from abc import ABC, abstractmethod
import inspect

from shared.InstantiatorMixin import InstantiatorMixin

#########################################################################################################
# ABSTRACT CLASS
#########################################################################################################


class Equipment(ABC, InstantiatorMixin):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @abstractmethod
    def provide_flows(self, *args, **kwargs) -> None:
        '''
        Implement in subclass with required parameters.
        '''
        pass

        return None
