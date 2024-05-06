import math


class PerfusionFilter():

    def __init__(self, innerDiam: int, length: float, surfaceArea: float, targetShearRate: float):
        self.innerDiam = innerDiam  # cm
        self.length = length  # cm
        self.surfaceArea = surfaceArea  # cm^2
        self.targetShearRate = targetShearRate  # s^-1
        self.numberOfLumen: int = round(
            self.surfaceArea / (2 * math.pi * (self.innerDiam / 2) * self.length), 0)
        self.targetRecicFlow: float = (self.targetShearRate * self.numberOfLumen * (
            math.pi * ((self.innerDiam / 2) ** 3))) * (3600 / 1000) / 4  # L/h

        self.perfusionFlow: float = None

        return None

    def provide_inflow(self, inflow):
        self.perfusionFlow = inflow
