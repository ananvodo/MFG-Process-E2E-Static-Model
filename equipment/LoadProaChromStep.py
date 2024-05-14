import math
from typing import Literal
from equipment.Equipment import Equipment
from equipment.SusvDiscr import SusvDiscr
from process_params.BioreactorParams import BioreactorParams
from process_params.ChromColumnParams import ChromColumnParams
from process_params.ChromResinParams import ChromResinParams
from process_params.ChromStepParams import ChromStepParams
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class LoadProaChromStep(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        flow: float,
        rt: float,
        time: float,
        volume: float,
        flowType: Literal['low', 'normal', 'high'] | None,
        loadMass: float,
        linearVel: float,
        cvs: float
    ) -> None:

        self.flow = flow  # in L/h
        self.rt = rt  # in minutes
        self.time = time  # in minutes
        self.volume = volume  # in L/cycle
        self.flowType: Literal['low', 'normal', 'high'] | None = flowType
        self.loadMass = loadMass  # in g
        self.linearVel = linearVel  # in cm/h
        self.cvs = cvs

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_params(
        cls,
        chromStepParams: ChromStepParams,
        susvDiscrProcess: SusvDiscr.Process,
        chromColumnParams: ChromColumnParams,
        bioreactorParams: BioreactorParams,
        chromResinParams: ChromResinParams
    ) -> 'LoadProaChromStep':

        flowType = susvDiscrProcess.flowType
        flow = susvDiscrProcess.outFlow
        linearVel = flow * Convert.LITERS_TO_MILLILITERS.value / \
            (math.pi * ((chromColumnParams.innerDiam / 2) ** 2))
        rt = (chromColumnParams.volume / flow) * Convert.HOURS_TO_MINUTES.value
        time = (chromResinParams.targetLoad * chromColumnParams.volume) / \
            (flow * bioreactorParams.titer) * Convert.HOURS_TO_MINUTES.value
        loadMass = chromColumnParams.volume * chromResinParams.targetLoad  # in g
        volume = loadMass / bioreactorParams.titer  # in L
        cvs = volume / chromColumnParams.volume

        # Create an instance of the class
        instance = cls(flow, rt, time, volume, flowType,
                       loadMass, linearVel, cvs)
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
            loadMass: {self.loadMass}
            linearVel: {self.linearVel}
            cvs: {self.cvs}'''
