from Equipment import Equipment


class Bioreactor(Equipment):

    def __init__(
        self,
        prodDays: int,
        titer: float,
        volume: int,
        vvd: int,
        bleedPercent: float
    ) -> None:
        # -------------------------------------
        # User defined attributes
        # -------------------------------------
        # BRX design parameters
        self.prodDays = prodDays  # number of days to produce
        self.titer = titer  # g/L of BRX
        self.volume = volume  # in L
        self.vvd = vvd
        self.bleedPercent = bleedPercent  # bleed is percentage
        self.outFlow: float = self.volume * self.vvd / \
            24  # in L/h. The 24 is to convert to h. This is really the perf flowrate
        self.inFlow: float = self.outFlow * \
            (1 + self.bleedPercent)  # in L/h. Media flowrate
        self.bleedFlow: float = self.outFlow * self.bleedPercent

        return None

    def provide_flows(self) -> None:
        return None
