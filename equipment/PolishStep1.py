from equipment.Chrom import Chrom
from equipment.BufferChromStep import BufferChromStep
from equipment.DepthFilterDiscr import DepthFilterDiscr
from equipment.Equipment import Equipment
from equipment.LoadPolishChromStep import LoadPolishChromStep
from process_params.ChromParams import ChromParams

#########################################################################################################
# CLASS
#########################################################################################################


class PolishStep1(Chrom):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        steps: list[BufferChromStep | LoadPolishChromStep],
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
    ) -> 'PolishStep1':

        return super().from_params(chromParams)

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def calculate_loading(
        self,
        chromParams: ChromParams,
        prevEquipment: Equipment,
    ) -> None:

        # the previous equipment is the depth filter
        depthFilterDiscr: DepthFilterDiscr = prevEquipment

        # Getting the normal inflow into the column
        for process in depthFilterDiscr.process:

            for step_params in chromParams.steps:
                if step_params.name in ('Loading', 'loading', 'Load', 'load'):
                    step = LoadPolishChromStep.from_params(
                        chromStepParams=step_params,
                        prevEquipmentProcess=process,
                        chromParams=chromParams,
                        prevEquipment=depthFilterDiscr,
                        nonLoadTime=self.nonLoadTime
                    )
                    self.steps.append(step)

        self.capturedMass = step.mass * chromParams.efficiency / 100  # g
        self.titer = self.capturedMass / step.volume  # g/L

        return None
