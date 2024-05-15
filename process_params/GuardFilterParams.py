from process_params.Params import Params

#########################################################################################################
# CLASS
#########################################################################################################


class GuardFilterParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        type: str,
        partNumber: str,
        area: float,
        quantity: int,
        loading: float,
    ) -> None:

        self.type = type  # This is the type of filter
        self.partNumber = partNumber  # This is the part number of the filter
        self.area = area  # in m^2
        self.quantity = quantity  # This is the number of filters in the system
        self.loading = loading  # Volume loaded in the filter in L/m^2
        self.totalArea = self.quantity * self.area  # m^2
        self.processVolume = self.totalArea * self.loading

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str
    ) -> 'GuardFilterParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}:
            type: {self.type}
            partNumber: {self.partNumber}
            area: {self.area}
            quantity: {self.quantity}
            loading: {self.loading}
            totalArea: {self.totalArea}
            processVolume: {self.processVolume}'''
