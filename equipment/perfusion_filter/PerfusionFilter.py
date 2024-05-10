import math
from typing import Literal
from equipment.Equipment import Equipment
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class PerfusionFilter(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        innerDiam: int,
        length: float,
        surfaceArea: float,
        targetShearRate: float
    ) -> None:
        # -------------------------------------
        # User defined attributes
        # -------------------------------------
        # Filter design parameters
        self.innerDiam = innerDiam  # cm
        self.length = length  # cm
        self.surfaceArea = surfaceArea  # cm^2
        self.targetShearRate = targetShearRate  # s^-1
        self.numberOfLumen: int = round(
            self.surfaceArea / (2 * math.pi * (self.innerDiam / 2) * self.length), 0)
        self.targetRecicFlow: float = (self.targetShearRate * self.numberOfLumen * (
            math.pi * ((self.innerDiam / 2) ** 3))) * Convert.MPS_TO_LPH.value / 4  # L/h

        # -------------------------------------
        # Calculated attributes
        # -------------------------------------
        # Flows
        self.inFlow: float = 0
        self.outFlow: float = 0

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}(
            innerDiam: {self.innerDiam}
            length: {self.length}
            surfaceArea: {self.surfaceArea}
            targetShearRate: {self.targetShearRate}
            numberOfLumen: {self.numberOfLumen}
            targetRecicFlow: {self.targetRecicFlow}
            inFlow: {self.inFlow}
            outFlow: {self.outFlow}
        )
        '''
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: Literal['PerfusionFilter', 'perfusionFilter'] = 'PerfusionFilter'
    ) -> 'PerfusionFilter':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def provide_flows(self, inflow: float) -> None:
        self.inFlow = inflow
        self.outFlow = inflow

        return None
