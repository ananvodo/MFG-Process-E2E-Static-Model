from process_params.Params import Params

###########################################################################################################
# CLASS
###########################################################################################################


class ViParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        stopHighVolumePercent: float,
        highVolumePercent: float,
        lowVolumePercent: float,
        stopLowVolumePercent: float,
        minWorkinfVolume: float,
        acidAdditionPercent: float,
        baseAdditionPercent: float,
        acidBuffer: str,
        baseBuffer: str,
        efficiency: float,
        reactionTime: float
    ) -> None:

        self.stopHighVolumePercent = stopHighVolumePercent  # %
        self.highVolumePercent = highVolumePercent  # %
        self.lowVolumePercent = lowVolumePercent  # %
        self.stopLowVolumePercent = stopLowVolumePercent  # %
        self.minWorkinfVolume = minWorkinfVolume  # L
        self.acidAdditionPercent = acidAdditionPercent  # %
        self.baseAdditionPercent = baseAdditionPercent  # %
        self.acidBuffer = acidBuffer
        self.baseBuffer = baseBuffer
        self.efficiency = efficiency
        self.reactionTime = reactionTime  # h

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str = 'VI'
    ) -> 'ViParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}:
            stopHighVolumePercent: {self.stopHighVolumePercent}
            highVolumePercent: {self.highVolumePercent}
            lowVolumePercent: {self.lowVolumePercent}
            stopLowVolumePercent: {self.stopLowVolumePercent}
            minWorkinfVolume: {self.minWorkinfVolume}
            acidAdditionPercent: {self.acidAdditionPercent}
            baseAdditionPercent: {self.baseAdditionPercent}
            acidBuffer: {self.acidBuffer}
            baseBuffer: {self.baseBuffer}
            efficiency: {self.efficiency}
            reactionTime: {self.reactionTime}'''
