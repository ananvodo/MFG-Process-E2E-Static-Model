from abc import ABC, abstractmethod


class Susv(ABC):

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
    ) -> None:

        # -------------------------------------
        # User defined attributes
        # -------------------------------------
        # Process parameters
        self.designVolume = designVolume  # in L. This is the max design volume of the SUSV
        self.phAdjustPercent = phAdjustPercent
        self.conductivityAdjustPercent = conductivityAdjustPercent
        self.flowPercentCompensation = flowPercentCompensation

        # Volume percentages
        self.stopHighVolumePercent = stopHighVolumePercent
        self.highVolumePercent = highVolumePercent
        self.normalVolumePercent = normalVolumePercent
        self.lowVolumePercent = lowVolumePercent
        self.stopLowVolumePercent = stopLowVolumePercent

        # Volume Volumes
        self.stopHighVolume: float = self.designVolume * self.stopHighVolumePercent / 100
        self.highVolume: float = self.designVolume * self.highVolumePercent / 100
        self.normalVolume: float = self.designVolume * self.normalVolumePercent / 100
        self.lowVolume: float = self.designVolume * self.lowVolumePercent / 100
        self.stopLowVolume: float = self.designVolume * self.stopLowVolumePercent / 100

        # -------------------------------------
        # Calculated attributes
        # -------------------------------------
        # Flows
        self.inFlow: float = 0
        self.lowOutFlow: float = 0
        self.outFlow: float = 0  # This is the normal outflow
        self.highOutFlow: float = 0

        # Residence times
        self.stopHighRt: float = 0
        self.highRt: float = 0
        self.normalRt: float = 0
        self.lowRt: float = 0
        self.stopLowRt: float = 0

        return None

    @abstractmethod
    def provide_flows(self) -> None:
        pass

        return None


class ContinuousSusv(Susv):

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


class SemiContinuousSusv(Susv):

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
