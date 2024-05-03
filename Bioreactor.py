class Bioreactor():

    def __init__(self, prodDays: int, titer: float, brxVol: int, vvd: int, bleedPercent: float):
        self.prodDays = prodDays  # number of days to produce
        self.titer = titer  # g/L of BRX
        self.brxVol = brxVol  # in L
        self.vvd = vvd
        self.bleedPercent = bleedPercent  # bleed is percentage
        self.outFlow: float = self.brxVol * self.vvd / \
            24  # in L/h. The 24 is to convert to h. This is really the perf flowrate
        self.mediaFeed: float = self.mediaFeed * (1 + self.bleedPercent)
        self.bleedFlow: float = self.mediaFeed * self.bleedPercent

        return None
