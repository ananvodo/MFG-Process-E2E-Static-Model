from __future__ import annotations
from typing import TYPE_CHECKING
import math
from process_data.Chrom import Chrom
from process_data.GuardFilterDiscr import GuardFilterDiscr
from process_data.SusvDiscr import SusvDiscr
from process_params.SusvDiscrParams import SusvDiscrParams
from shared.UnitConverter import UnitConverter as Convert

if TYPE_CHECKING:
    from process_params.ChromParams import ChromParams

#########################################################################################################
# CLASS
#########################################################################################################


class SemiContSusvDiscr(SusvDiscr):
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
        prevEquipment: GuardFilterDiscr | Chrom,
        chromParams: ChromParams
    ) -> 'SemiContSusvDiscr':

        # Calculating needed parameters
        # --------------------------------
        columnVolume = chromParams.column.volume
        resinTargetLoad = chromParams.resin.targetLoad
        columnInnerDiam = chromParams.column.innerDiam
        titrationVolumefactor: float = (1 + susvDiscrParams.phAdjustPercent / 100) * (
            1 + susvDiscrParams.conductivityAdjustPercent / 100)

        # Reading the inflow and titer
        # -----------------------------
        if isinstance(prevEquipment, GuardFilterDiscr):
            inFlow: float = [process.outFlow for process in prevEquipment.process if process.flowType ==
                             'normal'][0] * titrationVolumefactor
            titer = prevEquipment.titer / titrationVolumefactor

        if isinstance(prevEquipment, Chrom):
            load_steps = [step for step in prevEquipment.steps if step.name in (
                'Load', 'load', 'Loading', 'loading')]
            inFlow: float = [step.flow for step in load_steps if step.flowType ==
                             'normal'][0] * titrationVolumefactor
            titer = prevEquipment.titer / titrationVolumefactor

        # Calculating the outflow
        # -----------------------
        # 1. Getting the nonload time
        nonLoadTime = 0  # in minutes

        for step_params in chromParams.steps:

            if step_params.name not in ('Loading', 'loading', 'Load', 'load', 'Storage'):
                flow = step_params.linearVel * math.pi * \
                    ((columnInnerDiam / 2) ** 2) * \
                    Convert.MILLILITERS_TO_LITERS.value
                time = (columnVolume * step_params.cvs /
                        flow) * Convert.HOURS_TO_MINUTES.value
                nonLoadTime += time

        # 2. Getting the loaded mass into the column
        loadMass = columnVolume * resinTargetLoad

        # 3. Getting the loaded volume into the column
        loadVolume = loadMass / titer

        # 4. Getting the flow into the column or SUSV outflow
        outFlow_calc = inFlow / \
            (1 - (inFlow * nonLoadTime *
             Convert.MINUTES_TO_HOURS.value / loadVolume))  # in L/h

        # Getting the process for the different flow types
        # -------------------------------------------------
        process: list[cls.Process] = []  # List of SusvDiscr.Process

        for flowType in susvDiscrParams.flowType:

            if flowType == 'low':

                outFlow: float = outFlow_calc * \
                    (1 - susvDiscrParams.flowPercentCompensation / 100)
                rt: float = susvDiscrParams.lowVolume / inFlow
                accumulatedVolumeInNoOutFlow = (
                    outFlow - inFlow) * nonLoadTime * Convert.MINUTES_TO_HOURS.value  # in L

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    accumulatedVolumeInNoOutFlow=accumulatedVolumeInNoOutFlow,
                    flowType=flowType
                )

            elif flowType == 'normal':
                outFlow: float = outFlow_calc
                rt: float = susvDiscrParams.normalVolume / inFlow
                accumulatedVolumeInNoOutFlow = (
                    outFlow - inFlow) * nonLoadTime * Convert.MINUTES_TO_HOURS.value  # in L

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    accumulatedVolumeInNoOutFlow=accumulatedVolumeInNoOutFlow,
                    flowType=flowType
                )

            else:  # flowType == 'high'
                outFlow: float = outFlow_calc * \
                    (1 + susvDiscrParams.flowPercentCompensation / 100)
                rt: float = susvDiscrParams.highVolume / inFlow
                accumulatedVolumeInNoOutFlow = (
                    outFlow - inFlow) * nonLoadTime * Convert.MINUTES_TO_HOURS.value  # in L

                instance = cls.Process(
                    inFlow=inFlow,
                    outFlow=outFlow,
                    rt=rt,
                    accumulatedVolumeInNoOutFlow=accumulatedVolumeInNoOutFlow,
                    flowType=flowType
                )

            process.append(instance)

        # Create an instance of the class
        instance = cls(titer=titer, process=process)
        # Calling load_params on the instance
        instance.load_params(susvDiscrParams)

        return instance
