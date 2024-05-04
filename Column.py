import math


class Column():

    def __init__(self, name, innerDiam, bedHeight, maxPorteinLoad, targetProteinLoad, numberOfCols, loadLv):
        self.name = name
        self.innerDiam = innerDiam
        self.bedHeight = bedHeight
        self.maxProteinLoad = maxPorteinLoad
        self.targetProteinLoad = targetProteinLoad
        self.numberOfCols = numberOfCols
        self.loadLv = loadLv
        self.colVol = math.pi * (self.innerDiam/2) ^ 2 * self.bedHeight

        return None


class ProaSbmColumn(Column):

    def __init__(self):
        super().__init__()

        return None
