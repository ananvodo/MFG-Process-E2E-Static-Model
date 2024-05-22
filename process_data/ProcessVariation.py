from __future__ import annotations
from abc import ABC, abstractmethod
from process_data.ProcessData import ProcessData


class ProcessVariation(ProcessData):
    class Process(ABC):
        def __init__(self) -> None:
            pass

    @property
    @abstractmethod
    def process(self) -> list[Process]:
        '''
        Implement in subclass to return a list of process steps.
        It accounts for the different flow types of the process.
        '''
        pass
