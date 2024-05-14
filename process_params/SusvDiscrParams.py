from process_params.SusvParams import SusvParams

#########################################################################################################
# CLASS
#########################################################################################################


class SusvDiscrParams(SusvParams):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        designVolume: float,
        phAdjustPercent: float,
        conductivityAdjustPercent: float,
        flowPercentCompensation: float,
        stopHighVolumePercent: float,
        highVolumePercent: float,
        normalVolumePercent: float,
        lowVolumePercent: float,
        stopLowVolumePercent: float
    ) -> None:

        super().__init__(
            designVolume=designVolume,
            phAdjustPercent=phAdjustPercent,
            conductivityAdjustPercent=conductivityAdjustPercent
        )
        self.flowPercentCompensation = flowPercentCompensation
        self.flowType: list[str] = ['low', 'normal', 'high']
        self.stopHighVolumePercent = stopHighVolumePercent
        self.highVolumePercent = highVolumePercent
        self.normalVolumePercent = normalVolumePercent
        self.lowVolumePercent = lowVolumePercent
        self.stopLowVolumePercent = stopLowVolumePercent

        self.stopHighVolume: float = self.designVolume * \
            self.stopHighVolumePercent / 100
        self.highVolume: float = self.designVolume * \
            self.highVolumePercent / 100
        self.normalVolume: float = self.designVolume * \
            self.normalVolumePercent / 100
        self.lowVolume: float = self.designVolume * \
            self.lowVolumePercent / 100
        self.stopLowVolume: float = self.designVolume * \
            self.stopLowVolumePercent / 100

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str
    ) -> 'SusvDiscrParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {super().__str__()}
            flowPercentCompensation = {self.flowPercentCompensation},
            flowType = {self.flowType},
            stopHighVolumePercent = {self.stopHighVolumePercent},
            highVolumePercent = {self.highVolumePercent},
            normalVolumePercent = {self.normalVolumePercent},
            lowVolumePercent = {self.lowVolumePercent},
            stopLowVolumePercent = {self.stopLowVolumePercent}
            stopHighVolume = {self.stopHighVolume},
            highVolume = {self.highVolume},
            normalVolume = {self.normalVolume},
            lowVolume = {self.lowVolume},
            stopLowVolume = {self.stopLowVolume}'''
