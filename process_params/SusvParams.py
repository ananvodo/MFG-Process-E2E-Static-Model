from process_params.Params import Params

#########################################################################################################
# CLASS
#########################################################################################################


class SusvParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        designVolume: float,
        phAdjustPercent: float,
        conductivityAdjustPercent: float
    ) -> None:

        self.designVolume = designVolume
        self.phAdjustPercent = phAdjustPercent
        self.conductivityAdjustPercent = conductivityAdjustPercent

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str
    ) -> 'SusvParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}:
            designVolume = {self.designVolume},
            phAdjustPercent = {self.phAdjustPercent},
            conductivityAdjustPercent = {self.conductivityAdjustPercent}'''
