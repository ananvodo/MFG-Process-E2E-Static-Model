from abc import ABC, abstractmethod
import math
from typing import Literal, Optional

from shared.InstantiatorMixin import InstantiatorMixin
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# ABSTRACT CLASS
#########################################################################################################


class ChromStep(ABC, InstantiatorMixin):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        name: str,
        linearVel: float | None,
        bufferName: str,
        bufferCost: float,
        cvs: float | None,
        holdTime: float | None = None,
    ) -> None:

        # -------------------------------------
        # User defined attributes
        # -------------------------------------
        # Design parameters
        self.name = name  # Name of the step
        self.linearVel = linearVel  # in cm/h
        self.bufferName = bufferName  # Name of the buffer
        self.bufferCost = bufferCost  # in USD/L
        self.cvs = cvs
        self.holdTime = holdTime  # in minutes

        # -------------------------------------
        # Calculated attributes
        # -------------------------------------
        self.rt: float = 0  # in minutes
        self.flow: float = 0  # in L/h
        self.time: float = 0  # in minutes/cycle
        self.volume: float = 0  # in L/cycle. Buffer or load volume

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str = 'steps'
    ) -> 'ChromStep':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}(
            name: {self.name}
            linearVel: {self.linearVel}
            bufferName: {self.bufferName}
            bufferCost: {self.bufferCost}
            cvs: {self.cvs}
            holdTime: {self.holdTime}
            rt: {self.rt}
            flow: {self.flow}
            time: {self.time}
            volume: {self.volume}
        )
        '''
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @abstractmethod
    def calc_params(self, *args, **kwargs) -> None:
        pass

        return None
