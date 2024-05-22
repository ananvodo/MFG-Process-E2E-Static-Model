from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING
from process_data.BufferChromStep import BufferChromStep
from process_data.ProcessData import ProcessData
from process_data.LoadChromStep import LoadChromStep
from process_params.ChromParams import ChromParams

if TYPE_CHECKING:
    from process_data.SusvDiscr import SusvDiscr
    from process_params.ChromParams import ChromParams

#########################################################################################################
# CLASS
#########################################################################################################


class Chrom(ProcessData):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        steps: list[BufferChromStep | LoadChromStep],
        nonLoadTime: float
    ) -> None:

        self.steps = steps
        self.nonLoadTime = nonLoadTime  # in minutes
        self.capturedMass: float | None = None  # g/cycle
        self.titer: float | None = None  # g/L per cycle

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_params(
        cls,
        chromParams: ChromParams,
    ) -> 'Chrom':

        # Getting the steps
        steps: list[BufferChromStep | LoadChromStep] = []
        nonLoadTime = 0  # in minutes

        for step_params in chromParams.steps:

            if step_params.name not in ('Loading', 'loading', 'Load', 'load'):
                step = BufferChromStep.from_params(
                    chromColumnParams=chromParams.column,
                    chromStepParams=step_params
                )

                if step_params.name != 'Storage':
                    nonLoadTime += step.time

            steps.append(step)

        # Create an instance of the class
        instance = cls(steps=steps, nonLoadTime=nonLoadTime)
        # Now you can call load_params on the instance
        instance.load_params(chromParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @abstractmethod
    def calculate_loading(
        self,
        chromParams: 'ChromParams',
        prevEquipment: 'SusvDiscr',
    ) -> 'Chrom':
        pass

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        steps_str = ",\n    ".join(str(step) for step in self.steps)
        # Making sure all the attributes from Equipment class are loaded
        efficiency = getattr(self, 'efficiency', None)
        column = getattr(self, 'column', None)
        resin = getattr(self, 'resin', None)

        return f'''{self.__class__.__name__}:
            capturedMass: {self.capturedMass}
            titer: {self.titer}
            nonLoadTime: {self.nonLoadTime}
            efficiency: {efficiency}
            column: {column}
            resin: {resin}
            steps: [\n{steps_str}\n          ]'''
