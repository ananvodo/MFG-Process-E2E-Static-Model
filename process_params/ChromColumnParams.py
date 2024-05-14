import math

from process_params.Params import Params
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class ChromColumnParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        innerDiam: float,
        bedHeight: float,
        quantity: int,
    ) -> None:

        self.innerDiam = innerDiam
        self.bedHeight = bedHeight
        self.quantity = quantity
        self.volume = math.pi * (self.innerDiam/2) ** 2 * \
            self.bedHeight * Convert.MILLILITERS_TO_LITERS.value  # in L

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str = 'column'
    ) -> 'ChromColumnParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}:
            innerDiam: {self.innerDiam}
            bedHeight: {self.bedHeight}
            quantity: {self.quantity}
            volume: {self.volume}'''
