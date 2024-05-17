import math
from typing import Literal
from equipment.DepthFilterDiscr import DepthFilterDiscr
from equipment.Equipment import Equipment
from equipment.LoadChromStep import LoadChromStep
from equipment.SusvDiscr import SusvDiscr
from process_params.BioreactorParams import BioreactorParams
from process_params.ChromColumnParams import ChromColumnParams
from process_params.ChromParams import ChromParams
from process_params.ChromResinParams import ChromResinParams
from process_params.ChromStepParams import ChromStepParams
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class LoadPolishChromStep(LoadChromStep):
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
        accumulatedVolumeNonLoadTime: float
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
        prevEquipmentProcess: DepthFilterDiscr.Process,
        chromParams: ChromParams,
        prevEquipment: DepthFilterDiscr,
        nonLoadTime: float  # in minutes
    ) -> 'LoadPolishChromStep':

       # the previous equipment is the depth filter
        prevEquipmentProcess: DepthFilterDiscr.Process = prevEquipmentProcess

        # Getting some parameters needed
        columnVolume = chromParams.column.volume
        resinTargetLoad = chromParams.resin.targetLoad
        titer = prevEquipment.titer
        columnInnerDiam = chromParams.column.innerDiam
        numberOfColumn = chromParams.column.quantity

        # Getting the column load outflow
        loadMass = columnVolume * resinTargetLoad
        loadVolume = loadMass / titer
        inflow = prevEquipmentProcess.outFlow  # in L/h. This is the inflow of SUSV3
        flow = inflow / \
            (1 - (inflow * nonLoadTime *
             Convert.MINUTES_TO_HOURS.value / loadVolume))  # in L/h
        accumulatedVolumeNonLoadTime = (
            flow - inflow) * nonLoadTime * Convert.MINUTES_TO_HOURS.value  # in L

        # Getting the rest of the calculated parameters
        flowType = prevEquipmentProcess.flowType
        linearVel = flow * Convert.LITERS_TO_MILLILITERS.value / \
            (math.pi * ((columnInnerDiam / 2) ** 2))
        rt = (columnVolume / flow) * Convert.HOURS_TO_MINUTES.value
        time = (resinTargetLoad * columnVolume) / \
            (flow * titer) * Convert.HOURS_TO_MINUTES.value
        totalTime = time + nonLoadTime  # in minutes
        mass = columnVolume * resinTargetLoad  # in g/cycle
        volume = mass / titer  # in L/cycle
        cvs = volume / columnVolume
        cyclesPerDay = 1 / \
            (totalTime * Convert.MINUTES_TO_DAYS.value)  # in cycles/day
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
            cyclesPerDayPerColumn=cyclesPerDayPerColumn,
            accumulatedVolumeNonLoadTime=accumulatedVolumeNonLoadTime
        )
        # Calling load_params on the instance
        instance.load_params(chromStepParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        # Make sure to include the class name in the string
        name = getattr(self, 'name', None)
        bufferName = getattr(self, 'bufferName', None)
        bufferCost = getattr(self, 'bufferCost', None)
        holdTime = getattr(self, 'holdTime', None)

        return f'''
        {self.__class__.__name__}:
            name: {name}
            bufferName: {bufferName}
            bufferCost: {bufferCost}
            holdTime: {holdTime}
            flow: {self.flow}
            rt: {self.rt}
            time: {self.time}
            volume: {self.volume}
            flowType: {self.flowType}
            mass: {self.mass}
            linearVel: {self.linearVel}
            cvs: {self.cvs}
            cyclesPerDay: {self.cyclesPerDay}
            cyclesPerDayPerColumn: {self.cyclesPerDayPerColumn}'''
