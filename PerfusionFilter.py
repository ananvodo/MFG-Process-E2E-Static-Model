import math
from UnitConverter import UnitConverter as Convert


class PerfusionFilter():

    def __init__(
        self,
        innerDiam: int,
        length: float,
        surfaceArea: float,
        targetShearRate: float
    ) -> None:
        # User defined attributes
        self.innerDiam = innerDiam  # cm
        self.length = length  # cm
        self.surfaceArea = surfaceArea  # cm^2
        self.targetShearRate = targetShearRate  # s^-1
        self.numberOfLumen: int = round(
            self.surfaceArea / (2 * math.pi * (self.innerDiam / 2) * self.length), 0)
        self.targetRecicFlow: float = (self.targetShearRate * self.numberOfLumen * (
            math.pi * ((self.innerDiam / 2) ** 3))) * Convert.MPS_TO_LPH.value / 4  # L/h

        # Calculated attributes
        self.inflow: float = 0
        self.outFlow: float = 0

        return None

    def provide_flows(self, inflow: float) -> None:
        self.inflow = inflow
        self.outFlow = inflow

        return None
