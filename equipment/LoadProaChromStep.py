import math
from typing import Literal
from equipment.LoadChromStep import LoadChromStep
from equipment.SusvDiscr import SusvDiscr
from process_params.ChromColumnParams import ChromColumnParams
from process_params.ChromParams import ChromParams
from process_params.ChromResinParams import ChromResinParams
from process_params.ChromStepParams import ChromStepParams
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class LoadProaChromStep(LoadChromStep):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        flow: float,
        rt: float,
        time: float,
        volume: float,
        flowType: Literal['low', 'normal', 'high'] | None,
        mass: float,  # in g/cycle
        linearVel: float,
        cvs: float,
        cyclesPerDay: float,
        cyclesPerDayPerColumn: float,
        accumulatedVolumeNonLoadTime: float = 0  # Proa load is continuous
    ) -> None:

        super().__init__(
            flow=flow,
            rt=rt,
            time=time,
            volume=volume,
            flowType=flowType,
            mass=mass,
            linearVel=linearVel,
            cvs=cvs,
            cyclesPerDay=cyclesPerDay,
            cyclesPerDayPerColumn=cyclesPerDayPerColumn,
            accumulatedVolumeNonLoadTime=accumulatedVolumeNonLoadTime
        )

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_params(
        cls,
        chromStepParams: ChromStepParams,
        prevEquipmentProcess: SusvDiscr.Process,
        chromParams: ChromParams,
        prevEquipment: SusvDiscr
    ) -> 'LoadProaChromStep':

       # the previous equipment is the depth filter
        susvDiscrProcess: SusvDiscr.Process = prevEquipmentProcess

        # Getting some parameters needed
        columnVolume = chromParams.column.volume
        resinTargetLoad = chromParams.resin.targetLoad
        titer = prevEquipment.titer
        columnInnerDiam = chromParams.column.innerDiam
        numberOfColumn = chromParams.column.quantity

        # Getting the calculated parameters
        flowType = susvDiscrProcess.flowType
        flow = susvDiscrProcess.outFlow
        linearVel = flow * Convert.LITERS_TO_MILLILITERS.value / \
            (math.pi * ((columnInnerDiam / 2) ** 2))
        rt = (columnVolume / flow) * Convert.HOURS_TO_MINUTES.value
        time = (resinTargetLoad * columnVolume) / \
            (flow * titer) * Convert.HOURS_TO_MINUTES.value
        mass = columnVolume * resinTargetLoad  # in g
        volume = mass / titer  # in L
        cvs = volume / columnVolume
        cyclesPerDay = 1 / \
            (time * Convert.MINUTES_TO_DAYS.value)  # in cycles/day
        cyclesPerDayPerColumn = cyclesPerDay / numberOfColumn  # in cycles/day/column

        # Create an instance of the class
        instance = cls(
            flow=flow,
            rt=rt,
            time=time,
            volume=volume,
            flowType=flowType,
            mass=mass,
            linearVel=linearVel,
            cvs=cvs,
            cyclesPerDay=cyclesPerDay,
            cyclesPerDayPerColumn=cyclesPerDayPerColumn
        )
        # Calling load_params on the instance
        instance.load_params(chromStepParams)

        return instance
