from __future__ import annotations
from typing import TYPE_CHECKING
import math
from process_data.ProcessData import ProcessData
from shared.UnitConverter import UnitConverter as Convert

if TYPE_CHECKING:
    from process_params.ChromColumnParams import ChromColumnParams
    from process_params.ChromStepParams import ChromStepParams

#########################################################################################################
# CLASS
#########################################################################################################


class BufferChromStep(ProcessData):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        name: str,
        flow: float,
        rt: float,
        time: float,
        volume: float
    ) -> None:

        self.name = name  # name of the step
        self.flow = flow  # in L/h
        self.rt = rt  # in minutes
        self.time = time  # in minutes
        self.volume = volume  # in L/cycle

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_params(
        cls,
        chromColumnParams: ChromColumnParams,
        chromStepParams: ChromStepParams
    ) -> BufferChromStep:

        name = chromStepParams.name
        flow = chromStepParams.linearVel * math.pi * \
            ((chromColumnParams.innerDiam / 2) ** 2) * \
            Convert.MILLILITERS_TO_LITERS.value
        rt = (chromColumnParams.volume / flow) * Convert.HOURS_TO_MINUTES.value
        time = rt * chromStepParams.cvs  # in minutes
        volume = chromColumnParams.volume * chromStepParams.cvs  # in L/cycle

        # Create an instance of the class
        instance = cls(
            name=name,
            flow=flow,
            rt=rt,
            time=time,
            volume=volume
        )
        # Calling load_params on the instance
        instance.load_params(chromStepParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        # Make sure to include the class name in the string
        bufferName = getattr(self, 'bufferName', None)
        bufferCost = getattr(self, 'bufferCost', None)
        holdTime = getattr(self, 'holdTime', None)
        linearVel = getattr(self, 'linearVel', None)
        cvs = getattr(self, 'cvs', None)

        return f'''
        {self.__class__.__name__}:
            name: {self.name}
            bufferName: {bufferName}
            bufferCost: {bufferCost}
            holdTime: {holdTime}
            cvs: {cvs}
            linearVel: {linearVel}
            flow: {self.flow}
            rt: {self.rt}
            time: {self.time}
            volume: {self.volume}'''
