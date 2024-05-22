from __future__ import annotations
from typing import Literal

from process_data.ProcessVariation import ProcessVariation

#########################################################################################################
# CLASS
#########################################################################################################


class SusvDiscr(ProcessVariation):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    class Process(ProcessVariation.Process):
        def __init__(
            self,
            inFlow: float,
            outFlow: float,
            rt: float,
            accumulatedVolumeInNoOutFlow: float,
            flowType: Literal['low', 'normal', 'high']
        ) -> None:

            self.inFlow = inFlow  # in L/min
            self.outFlow = outFlow  # in L/min
            self.rt = rt  # in minutes
            self.accumulatedVolumeInNoOutFlow = accumulatedVolumeInNoOutFlow  # in L
            self.flowType = flowType

            return None

        def __str__(self) -> str:
            return f'''
            {self.__class__.__name__}:
                inFlow: {self.inFlow}
                outFlow: {self.outFlow}
                rt: {self.rt}
                accumulatedVolumeInNoOutFlow: {self.accumulatedVolumeInNoOutFlow}
                flowType: {self.flowType}'''

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        titer: float,
        process: list[Process],
    ) -> None:

        self.titer = titer  # in g/L
        self.process = process

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @property
    def process(self) -> list[SusvDiscr.Process]:
        return self._process

    @process.setter
    def process(self, value: list[SusvDiscr.Process]) -> None:
        self._process = value
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        process_str = ",\n    ".join(str(step) for step in self.process)

        # # Making sure all the attributes from Params class are loaded
        flowPercentCompensation = getattr(
            self, 'flowPercentCompensation', None)
        flowType = getattr(self, 'flowType', None)
        stopHighVolumePercent = getattr(self, 'stopHighVolumePercent', None)
        highVolumePercent = getattr(self, 'highVolumePercent', None)
        normalVolumePercent = getattr(self, 'normalVolumePercent', None)
        lowVolumePercent = getattr(self, 'lowVolumePercent', None)
        stopLowVolumePercent = getattr(self, 'stopLowVolumePercent', None)
        stopHighVolume = getattr(self, 'stopHighVolume', None)
        highVolume = getattr(self, 'highVolume', None)
        normalVolume = getattr(self, 'normalVolume', None)
        lowVolume = getattr(self, 'lowVolume', None)
        stopLowVolume = getattr(self, 'stopLowVolume', None)

        return f'''
        {self.__class__.__name__}:
            flowPercentCompensation: {flowPercentCompensation}
            flowType: {flowType}
            stopHighVolumePercent: {stopHighVolumePercent}
            highVolumePercent: {highVolumePercent}
            normalVolumePercent: {normalVolumePercent}
            lowVolumePercent: {lowVolumePercent}
            stopLowVolumePercent: {stopLowVolumePercent}
            stopHighVolume: {stopHighVolume}
            highVolume: {highVolume}
            normalVolume: {normalVolume}
            lowVolume: {lowVolume}
            stopLowVolume: {stopLowVolume}
            process:[\n{process_str}\n           ]'''
