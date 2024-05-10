
from equipment.susv import Susv

#########################################################################################################
# CLASS
#########################################################################################################


class SemiContinuousSusv(Susv):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        flowPercentCompensation: float,
        designVolume: float,
        stopHighVolumePercent: float,
        highVolumePercent: float,
        normalVolumePercent: float,
        lowVolumePercent: float,
        stopLowVolumePercent: float,
        phAdjustPercent: float,
        conductivityAdjustPercent: float
    ):
        super().__init__(
            flowPercentCompensation,
            designVolume,
            stopHighVolumePercent,
            highVolumePercent,
            normalVolumePercent,
            lowVolumePercent,
            stopLowVolumePercent,
            phAdjustPercent,
            conductivityAdjustPercent
        )

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str  # it can be Susv1, Susv2, etc.
    ) -> 'SemiContinuousSusv':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def provide_flows(self, inflow: float, outFlow: float | None = None):
        self.inFlow: float = inflow * \
            (1 + self.phAdjustPercent / 100 + self.conductivityAdjustPercent / 100)
        self.normalOutFlow: float = self.inFlow * \
            (1 + self.phAdjustPercent / 100 + self.conductivityAdjustPercent / 100)
        self.lowOutFlow: float = self.normalOutFlow * \
            (1 - self.flowPercentCompensation)
        self.highOutFlow: float = self.normalOutFlow * \
            (1 + self.flowPercentCompensation)

        return None
