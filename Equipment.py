from abc import ABC, abstractmethod


class Equipment(ABC):

    @abstractmethod
    def provide_flows(self, *args, **kwargs):
        '''
        Implement in subclass with required parameters.
        '''
        pass
