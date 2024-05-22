from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Literal

from process_data.ProcessData import ProcessData

if TYPE_CHECKING:
    from process_params.PerfusionFilterParams import PerfusionFilterParams
    from process_data.Bioreactor import Bioreactor

#########################################################################################################
# CLASS
#########################################################################################################


class PerfusionFilter(ProcessData):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        titer: float,
        inFlow: float,
        outFlow: float,
    ) -> None:

        self.titer: float = titer  # in g/L
        self.inFlow = inFlow  # L/h
        self.outFlow = outFlow  # L/h

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        bioreactor: Bioreactor,
        perfusionFilterParams: PerfusionFilterParams,
    ) -> PerfusionFilter:

        inFlow: float = bioreactor.outFlow
        outFlow: float = bioreactor.outFlow
        titer: float = bioreactor.titer

        # Create an instance of the class
        instance = cls(
            titer=titer,
            inFlow=inFlow,
            outFlow=outFlow,
        )
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
