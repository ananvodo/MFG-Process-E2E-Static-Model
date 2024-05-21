from equipment.Chrom import Chrom
from equipment.BufferChromStep import BufferChromStep
from equipment.Equipment import Equipment
from equipment.LoadChromStep import LoadChromStep
from equipment.SusvDiscr import SusvDiscr
from process_params.ChromParams import ChromParams

#########################################################################################################
# CLASS
#########################################################################################################


class Proa(Chrom):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        steps: list[BufferChromStep | LoadChromStep],
        nonLoadTime: float
    ) -> None:

        super().__init__(
            steps=steps,
            nonLoadTime=nonLoadTime
        )

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_params(
        cls,
        chromParams: ChromParams,
    ) -> 'Proa':

        return super().from_params(chromParams)

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def calculate_loading(
        self,
        chromParams: ChromParams,
        prevEquipment: Equipment,
    ) -> 'Proa':

        # the previous equipment is the SUSV1
        susvDiscr: SusvDiscr = prevEquipment  # this is to provide type hinting

        for process in susvDiscr.process:

            for step_params in chromParams.steps:
                if step_params.name in ('Loading', 'loading', 'Load', 'load'):
                    step = LoadChromStep.from_params(
                        chromStepParams=step_params,
                        prevEquipmentProcess=process,
                        chromParams=chromParams,
                        prevEquipment=susvDiscr
                    )
                    self.steps.append(step)

        # Calculate the mass captured
        elution_step = [step for step in self.steps if step.name in (
            'Elution', 'elution', 'Elute', 'elute')][0]

        load_step = [step for step in self.steps if step.name in (
            'Loading', 'loading', 'Load', 'load')][0]  # all load steps capture the same mass

        self.capturedMass = load_step.mass * chromParams.efficiency / 100  # g
        self.titer = self.capturedMass / elution_step.volume  # g/L

        return None
