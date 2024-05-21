from typing import Literal
from equipment.Bioreactor import Bioreactor
from equipment.Equipment import Equipment
from process_params.PerfusionFilterParams import PerfusionFilterParams

#########################################################################################################
# CLASS
#########################################################################################################


class PerfusionFilter(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    class Process():
        def __init__(
            self,
            inFlow: float,
            outFlow: float,
            flowType: Literal['low', 'normal', 'high'] = 'normal'
        ) -> None:

            self.inFlow = inFlow  # L/h
            self.outFlow = outFlow  # L/h
            self.flowType = flowType  # Options: 'low', 'normal', 'high'

            return None

        def __str__(self) -> str:
            return f'''
            {self.__class__.__name__}:
                inFlow: {self.inFlow}
                outFlow: {self.outFlow}'''

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        titer: float,
        process: list[Process],
    ) -> None:

        self.titer: float = titer  # in g/L
        self.process = process

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        bioreactor: Bioreactor,
        perfusionFilterParams: PerfusionFilterParams,
    ) -> 'PerfusionFilter':

        process: list[cls.Process] = []

        inFlow: float = bioreactor.outFlow
        outFlow: float = bioreactor.outFlow
        titer: float = bioreactor.titer

        process.append(cls.Process(inFlow=inFlow, outFlow=outFlow))

        # Create an instance of the class
        instance = cls(process=process, titer=titer)
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
            outFlow: {self.outFlow}
            titrer: {self.titer}'''
