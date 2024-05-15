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
        uspLowFlowCompensationPercent: float,
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
        self.uspLowFlowCompensationPercent = uspLowFlowCompensationPercent  # %
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

        # Calculated variables
        self.stopHighMass = self.minWorkinfVolume * \
            (1 + self.stopHighVolumePercent / 100)
        self.highMassUspSwitchLow = self.minWorkinfVolume * \
            (1 + self.uspLowFlowCompensationPercent / 100)
        self.highMass = self.minWorkinfVolume * \
            (1 + self.highVolumePercent / 100)
        self.LowMass = self.minWorkinfVolume * \
            (1 - self.lowVolumePercent / 100)
        self.lowLowMass = self.minWorkinfVolume * \
            (1 - self.stopLowVolumePercent / 100)

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
            stopHighVolumePercent: {self.stopHighVolumePercent}%
            upsLowFlowCompPercent: {self.upsLowFlowCompPercent}%
            highLevelCompPercent: {self.highLevelCompPercent}%
            LowLevelPercent: {self.LowLevelPercent}%
            lowLowLevelCompPercent: {self.lowLowLevelCompPercent}%
            minWorkinfVolume: {self.minWorkinfVolume} L
            acidAdditionPercent: {self.acidAdditionPercent}%
            baseAdditionPercent: {self.baseAdditionPercent}%
            acidBuffer: {self.acidBuffer}
            baseBuffer: {self.baseBuffer}
            efficiency: {self.efficiency}
            reactionTime: {self.reactionTime}
            stopHighMass: {self.stopHighMass}
            highMassUspSwitchLow: {self.highMassUspSwitchLow}
            highMass: {self.highMass}
            LowMass: {self.LowMass}
            lowLowMass: {self.lowLowMass}'''
