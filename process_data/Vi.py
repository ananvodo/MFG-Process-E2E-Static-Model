from __future__ import annotations
from typing import TYPE_CHECKING
import math
from typing import Literal
from process_data.ProcessData import ProcessData
from process_data.ProcessVariation import ProcessVariation
from shared.UnitConverter import UnitConverter as Convert

if TYPE_CHECKING:
    from process_params.BioreactorParams import BioreactorParams
    from process_data.Proa import Proa
    from process_params.ViParams import ViParams

###########################################################################################################
# CLASS
###########################################################################################################


class Vi(ProcessVariation):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    class Process(ProcessVariation.Process):
        def __init__(
            self,
            time: float,
            cyclesPerDay: float,
            cyclesPerRun: float,
            inFlow: float,
            outFlow: float,
            flowType: Literal['low', 'normal', 'high']
        ) -> None:

            self.time = time  # h
            self.cyclesPerDay = cyclesPerDay
            self.cyclesPerRun = cyclesPerRun
            self.inFlow = inFlow  # L/h
            self.outFlow = outFlow  # L/h
            self.flowType = flowType  # low, normal, high

            return None

        def __str__(self) -> str:
            return f'''
            {self.__class__.__name__}:
                time: {self.time}
                cyclesPerDay: {self.cyclesPerDay}
                cyclesPerRun: {self.cyclesPerRun}
                inFlow: {self.inFlow}
                outFlow: {self.outFlow}
                flowType: {self.flowType}'''
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __init__(
        self,
        elutionCycles: float,
        volume: float,
        titer: float,
        mass: float,
        process: list[Process],
    ) -> None:

        self.elutionCycles = elutionCycles
        self.volume = volume  # L
        self.titer = titer  # g/L
        self.mass = mass  # g
        self.process = process

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @property
    def process(self) -> list[Vi.Process]:
        return self._process

    @process.setter
    def process(self, value: list[Vi.Process]) -> None:
        self._process = value
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        viParams: ViParams,
        proa: Proa,
        bioreactorParams: BioreactorParams,
    ) -> Vi:

        # Getting the elution cycles
        elution_step = [step for step in proa.steps if step.name in (
            'Elution', 'elution', 'Elute', 'elute')][0]
        elutionCycles = math.ceil(
            viParams.minWorkinfVolume / elution_step.volume)

        # Getting the vi total volume
        elution_volume = elution_step.volume * elutionCycles  # L
        volume = elution_volume * \
            (1 + viParams.acidAdditionPercent / 100) * \
            (1 + viParams.baseAdditionPercent / 100)

        # Getting the vi mass
        mass = proa.capturedMass * elutionCycles * viParams.efficiency / 100  # g
        titer = mass / volume  # g/L

        # Getting the process
        process: list[cls.Process] = []  # List of Process instances
        loading_steps = [step for step in proa.steps if step.name in (
            'Loading', 'loading', 'Load', 'load')]

        for step in loading_steps:
            time = step.time * Convert.MINUTES_TO_HOURS.value * \
                elutionCycles + viParams.reactionTime
            cyclesPerDay = 1 / \
                (time * Convert.HOURS_TO_DAYS.value)  # cycles/day
            cyclesPerRun = bioreactorParams.prodDays * cyclesPerDay
            outFlow = volume / time  # L/h
            flowType = step.flowType

            process.append(
                cls.Process(
                    time=time,
                    cyclesPerDay=cyclesPerDay,
                    cyclesPerRun=cyclesPerRun,
                    inFlow=outFlow,
                    outFlow=outFlow,
                    flowType=flowType
                )
            )

        # Create an instance of the class
        instance = cls(
            elutionCycles=elutionCycles,
            volume=volume,
            titer=titer,
            mass=mass,
            process=process
        )
        # Calling load_params on the instance
        instance.load_params(viParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        process_str = ",\n    ".join(str(step) for step in self.process)

        # # Making sure all the attributes from Params class are loaded
        stopHighVolumePercent = getattr(self, 'stopHighVolumePercent', None)
        highVolumePercent = getattr(self, 'highVolumePercent', None)
        lowVolumePercent = getattr(self, 'lowVolumePercent', None)
        stopLowVolumePercent = getattr(self, 'stopLowVolumePercent', None)
        minWorkinfVolume = getattr(self, 'minWorkinfVolume', None)
        acidAdditionPercent = getattr(self, 'acidAdditionPercent', None)
        baseAdditionPercent = getattr(self, 'baseAdditionPercent', None)
        acidBuffer = getattr(self, 'acidBuffer', None)
        baseBuffer = getattr(self, 'baseBuffer', None)
        efficiency = getattr(self, 'efficiency', None)
        reactionTime = getattr(self, 'reactionTime', None)

        return f'''
        {self.__class__.__name__}:
            stopHighVolumePercent: {stopHighVolumePercent}
            highVolumePercent: {highVolumePercent}
            lowVolumePercent: {lowVolumePercent}
            stopLowVolumePercent: {stopLowVolumePercent}
            minWorkinfVolume: {minWorkinfVolume}
            acidAdditionPercent: {acidAdditionPercent}
            baseAdditionPercent: {baseAdditionPercent}
            acidBuffer: {acidBuffer}
            baseBuffer: {baseBuffer}
            efficiency: {efficiency}
            reactionTime: {reactionTime}
            elutionCycles: {self.elutionCycles}
            volume: {self.volume},
            mass: {self.mass},
            titer: {self.titer},
            process:[\n{process_str}\n           ]'''
