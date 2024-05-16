from process_params.Params import Params
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class DepthFilterParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        type: str,
        partNumber: str,
        area: float,
        quantity: int,
        loading: float,
        bufferFlushLoading: float,
        bufferFlushFlux: float,
        effiency: float
    ) -> None:

        self.type = type  # This is the type of filter
        self.partNumber = partNumber
        self.area = area  # in m^2
        self.quantity = quantity  # This is the number of filters in the system
        self.loading = loading  # in L/m^2
        self.bufferFlushLoading = bufferFlushLoading  # in L/m^2
        self.bufferFlushFlux = bufferFlushFlux  # in L/m^2/h
        self.effiency = effiency  # in %

        self.totalArea = self.quantity * self.area  # m^2
        self.bufferFlushVolume = self.totalArea * self.bufferFlushLoading  # in L
        self.bufferFlushTime = (
            self.bufferFlushVolume / self.bufferFlushFlux) * Convert.HOURS_TO_SECONDS.value  # in s
        self.processVolume = self.totalArea * self.loading  # in L

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str
    ) -> 'DepthFilterParams':

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
            bufferFlushLoading: {self.bufferFlushLoading}
            bufferFlushFlux: {self.bufferFlushFlux}
            totalArea: {self.totalArea}
            bufferFlushVolume: {self.bufferFlushVolume}
            bufferFlushTime: {self.bufferFlushTime}
            processVolume: {self.processVolume}'''
