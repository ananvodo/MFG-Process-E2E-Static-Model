from equipment.susv.Susv import Susv

#########################################################################################################
# CLASS
#########################################################################################################


class ContinuousSusv(Susv):
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

    def provide_flows(self, inflow: float):
        self.inFlow: float = inflow
        self.outFlow: float = self.inFlow

        self.lowOutFlow: float = self.outFlow * \
            (1 - self.flowPercentCompensation / 100)
        self.highOutFlow: float = self.outFlow * \
            (1 + self.flowPercentCompensation / 100)

        self.stopHighRt: float = self.stopHighVolume / self.inFlow
        self.highRt: float = self.highVolume / self.inFlow
        self.normalRt: float = self.normalVolume / self.inFlow
        self.lowRt: float = self.lowVolume / self.inFlow
        self.stopLowRt: float = self.stopLowVolume / self.inFlow

        return None
