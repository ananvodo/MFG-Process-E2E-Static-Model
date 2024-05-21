from equipment.Chrom import Chrom
from equipment.BufferChromStep import BufferChromStep
from equipment.LoadChromStep import LoadChromStep
from equipment.SemiContSusvDiscr import SemiContSusvDiscr
from process_params.ChromParams import ChromParams

#########################################################################################################
# CLASS
#########################################################################################################


class PolishStep(Chrom):
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
    ) -> 'PolishStep':

        return super().from_params(chromParams)

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def calculate_loading(
        self,
        chromParams: ChromParams,
        prevEquipment: SemiContSusvDiscr,
    ) -> None:

        # the previous equipment is really the SUSV3 equipment.
        # The problem is that SUSV3 equipment outFlow is defined by the PS equipment.
        # The outFlow of the SUSV3 feed the PS equipment, which is defined by the column size and resin.
        # The SUSV3 normal

        # Getting the normal inflow into the column
        for process in prevEquipment.process:
            process: SemiContSusvDiscr.Process

            for step_params in chromParams.steps:

                if step_params.name in ('Loading', 'loading', 'Load', 'load'):
                    step = LoadChromStep.from_params(
                        chromStepParams=step_params,
                        prevEquipmentProcess=process,
                        chromParams=chromParams,
                        prevEquipment=prevEquipment,
                    )
                    self.steps.append(step)

        wash_collection_volume = [
            step.volume for step in self.steps if step.name == 'Wash Collection'][0]
        self.capturedMass = step.mass * chromParams.efficiency / 100  # g
        volume_total = step.volume + wash_collection_volume
        self.titer = self.capturedMass / volume_total  # g/L

        return None
