import math


class Column():

    def __init__(
        self,
        innerDiam: float,
        bedHeight: float,
        numberOfCols: int,
    ) -> None:

        self.innerDiam = innerDiam
        self.bedHeight = bedHeight
        self.numberOfCols = numberOfCols
        self.colVol = math.pi * (self.innerDiam/2) ^ 2 * self.bedHeight

        return None


class ProaSbmColumn(Column):

    def __init__(self):
        super().__init__()

        return None
