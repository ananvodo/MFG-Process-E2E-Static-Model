from typing import Literal

from process_params.Params import Params

#########################################################################################################
# CLASS
#########################################################################################################


class BioreactorParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
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
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: Literal['Bioreactor', 'bioreactor'] = 'Bioreactor'
    ) -> 'BioreactorParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}:
            prodDays: {self.prodDays}
            titer: {self.titer}
            volume: {self.volume}
            vvd: {self.vvd}
            bleedPercent: {self.bleedPercent}
            outFlow: {self.outFlow}
            inFlow: {self.inFlow}
            bleedFlow: {self.bleedFlow}'''
