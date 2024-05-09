import math

from UnitConverter import UnitConverter as Convert


class Column():

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

    def __str__(self):
        return (f"{self.__class__.__name__}(innerDiam={self.innerDiam} cm, bedHeight={self.bedHeight} cm, "
                f"quantity={self.quantity}, volume={self.volume:.2f} L)")


class ProaSbmColumn(Column):

    def __init__(
        self,
        innerDiam: float,
        bedHeight: float,
        quantity: int,
    ) -> None:

        super().__init__(
            innerDiam=innerDiam,
            bedHeight=bedHeight,
            quantity=quantity,
        )

        return None

    def __str__(self):
        return super().__str__()
