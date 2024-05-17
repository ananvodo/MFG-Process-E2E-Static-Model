from typing import Literal
from equipment.Equipment import Equipment

#########################################################################################################
# CLASS
#########################################################################################################


class LoadChromStep(Equipment):
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
        cyclesPerDayPerColumn: float,
        accumulatedVolumeNonLoadTime: float
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
        # Volume accumulated in the SUSVduring non-load time
        self.accumulatedVolumeNonLoadTime = accumulatedVolumeNonLoadTime  # in L

        return None

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
