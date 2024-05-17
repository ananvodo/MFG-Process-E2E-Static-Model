from typing import Literal
from equipment.Equipment import Equipment
from equipment.PerfusionFilter import PerfusionFilter
from process_params.SusvDiscrParams import SusvDiscrParams


#########################################################################################################
# CLASS
#########################################################################################################


class SusvDiscr(Equipment):

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    class Process():
        def __init__(
            self,
            inFlow: float,
            outFlow: float,
            rt: float,
            flowType: Literal['low', 'normal', 'high']
        ) -> None:

            self.inFlow = inFlow
            self.outFlow = outFlow
            self.rt = rt
            self.flowType = flowType

            return None

        def __str__(self) -> str:
            return f'''
            {self.__class__.__name__}:
                inFlow: {self.inFlow}
                outFlow: {self.outFlow}
                rt: {self.rt}
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
    @classmethod
    def from_params(
        cls,
        susvDiscrParams: SusvDiscrParams,
        prevEquipment: Equipment
    ) -> 'SusvDiscr':

        titrationVolumefactor: float = (1 + susvDiscrParams.phAdjustPercent / 100) * (
            1 + susvDiscrParams.conductivityAdjustPercent / 100)
        inFlow: float = prevEquipment.outFlow * titrationVolumefactor

        titer = prevEquipment.titer / titrationVolumefactor

        process = []

        for flowType in susvDiscrParams.flowType:

            if flowType == 'low':
                outFlow: float = inFlow * \
                    (1 - susvDiscrParams.flowPercentCompensation / 100)
                rt: float = susvDiscrParams.lowVolume / inFlow

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    flowType=flowType
                )

            elif flowType == 'normal':
                outFlow: float = inFlow
                rt: float = susvDiscrParams.normalVolume / inFlow

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    flowType=flowType
                )

            else:  # flowType == 'high'
                outFlow: float = inFlow * \
                    (1 + susvDiscrParams.flowPercentCompensation / 100)
                rt: float = susvDiscrParams.highVolume / inFlow

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    flowType=flowType
                )

            process.append(instance)

        # Create an instance of the class
        instance = cls(titer=titer, process=process)
        # Calling load_params on the instance
        instance.load_params(susvDiscrParams)

        return instance

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
