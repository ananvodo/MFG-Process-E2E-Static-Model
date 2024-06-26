from __future__ import annotations
from typing import TYPE_CHECKING
import math
from typing import Literal
from process_data.ProcessData import ProcessData
from shared.UnitConverter import UnitConverter as Convert

if TYPE_CHECKING:
    from process_data.SusvDiscr import SusvDiscr
    from process_params.ChromParams import ChromParams
    from process_params.ChromStepParams import ChromStepParams

#########################################################################################################
# CLASS
#########################################################################################################


class LoadChromStep(ProcessData):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        flow: float,
        rt: float,
        time: float,
        volume: float,
        flowType: Literal['low', 'normal', 'high'] | None,
        mass: float,
        linearVel: float,
        cvs: float,
        cyclesPerDay: float,
        cyclesPerDayPerColumn: float
    ) -> None:

        self.flow = flow  # in L/h
        self.rt = rt  # in minutes
        self.time = time  # in minutes
        self.volume = volume  # in L/cycle
        self.flowType: Literal['low', 'normal', 'high'] | None = flowType
        self.mass = mass  # in g of protein/cycle
        self.linearVel = linearVel  # in cm/h
        self.cvs = cvs
        self.cyclesPerDay = cyclesPerDay  # in cycles/day
        self.cyclesPerDayPerColumn = cyclesPerDayPerColumn  # in cycles/day/column

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
    ) -> LoadChromStep:

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
