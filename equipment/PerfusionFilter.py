from equipment.Bioreactor import Bioreactor
from equipment.Equipment import Equipment
from process_params.PerfusionFilterParams import PerfusionFilterParams

#########################################################################################################
# CLASS
#########################################################################################################


class PerfusionFilter(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        inFlow: float,
        outFlow: float,
    ) -> None:

        self.inFlow: float = inFlow
        self.outFlow: float = outFlow

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        bioreactor: Bioreactor,
        perfusionFilterParams: PerfusionFilterParams,
    ) -> 'PerfusionFilter':

        inFlow: float = bioreactor.outFlow
        outFlow: float = bioreactor.outFlow

        # Create an instance of the class
        instance = cls(inFlow, outFlow)
        # Now you can call load_params on the instance
        instance.load_params(perfusionFilterParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        innerDiam = getattr(self, 'innerDiam', None)
        length = getattr(self, 'length', None)
        surfaceArea = getattr(self, 'surfaceArea', None)
        targetShearRate = getattr(self, 'targetShearRate', None)
        numberOfLumen = getattr(self, 'numberOfLumen', None)
        targetRecicFlow = getattr(self, 'targetRecicFlow', None)

        return f'''
        {self.__class__.__name__}:
            innerDiam: {innerDiam}
            length: {length}
            surfaceArea: {surfaceArea}
            targetShearRate: {targetShearRate}
            numberOfLumen: {numberOfLumen}
            targetRecicFlow: {targetRecicFlow}
            inFlow: {self.inFlow}
            outFlow: {self.outFlow}'''
