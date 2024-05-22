from __future__ import annotations
from typing import TYPE_CHECKING
from process_data.SusvDiscr import SusvDiscr
from process_data.Chrom import Chrom
from process_data.PerfusionFilter import PerfusionFilter
from process_data.Vi import Vi
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################
if TYPE_CHECKING:
    from process_params.SusvDiscrParams import SusvDiscrParams


class ContSusvDiscr(SusvDiscr):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        titer: float,
        process: list[SusvDiscr.Process],
    ) -> None:

        super().__init__(
            titer=titer,
            process=process
        )

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_params(
        cls,
        susvDiscrParams: SusvDiscrParams,
        prevEquipment: PerfusionFilter | Vi | Chrom
    ) -> ContSusvDiscr:

        titrationVolumefactor: float = (1 + susvDiscrParams.phAdjustPercent / 100) * (
            1 + susvDiscrParams.conductivityAdjustPercent / 100)
        titer = prevEquipment.titer / titrationVolumefactor

        if isinstance(prevEquipment, Vi):
            inFlow: float = [process.outFlow for process in prevEquipment.process if process.flowType ==
                             'normal'][0] * titrationVolumefactor

        if isinstance(prevEquipment, PerfusionFilter):
            inFlow: float = prevEquipment.outFlow * titrationVolumefactor

        if isinstance(prevEquipment, Chrom):
            load_normal = [step for step in prevEquipment.steps if step.name in (
                'Load', 'load', 'Loading', 'loading') and step.flowType == 'normal'][0]
            loaded_volume: float = load_normal.volume * titrationVolumefactor
            cycle_time: float = load_normal.time
            nonload_time: float = prevEquipment.nonLoadTime
            total_time: float = (cycle_time + nonload_time) * \
                Convert.MINUTES_TO_HOURS.value
            inFlow: float = loaded_volume / total_time

        # Calculating the process instances
        process: list[cls.Process] = []  # List of SusvDiscr.Process

        for flowType in susvDiscrParams.flowType:

            if flowType == 'low':
                outFlow: float = inFlow * \
                    (1 - susvDiscrParams.flowPercentCompensation / 100)
                rt: float = susvDiscrParams.lowVolume / inFlow

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    accumulatedVolumeInNoOutFlow=0,
                    flowType=flowType
                )

            elif flowType == 'normal':
                outFlow: float = inFlow
                rt: float = susvDiscrParams.normalVolume / inFlow

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    accumulatedVolumeInNoOutFlow=0,
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
                    accumulatedVolumeInNoOutFlow=0,
                    flowType=flowType
                )

            process.append(instance)

        # Create an instance of the class
        instance = cls(titer=titer, process=process)
        # Calling load_params on the instance
        instance.load_params(susvDiscrParams)

        return instance
