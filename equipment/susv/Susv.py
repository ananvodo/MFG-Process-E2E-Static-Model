from abc import abstractmethod

from equipment.Equipment import Equipment

#########################################################################################################
# CLASS
#########################################################################################################


class Susv(Equipment):
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
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}(
            designVolume: {self.designVolume}
            phAdjustPercent: {self.phAdjustPercent}
            conductivityAdjustPercent: {self.conductivityAdjustPercent}
            flowPercentCompensation: {self.flowPercentCompensation}
            stopHighVolumePercent: {self.stopHighVolumePercent}
            highVolumePercent: {self.highVolumePercent}
            normalVolumePercent: {self.normalVolumePercent}
            lowVolumePercent: {self.lowVolumePercent}
            stopLowVolumePercent: {self.stopLowVolumePercent}
            stopHighVolume: {self.stopHighVolume}
            highVolume: {self.highVolume}
            normalVolume: {self.normalVolume}
            lowVolume: {self.lowVolume}
            stopLowVolume: {self.stopLowVolume}
            inFlow: {self.inFlow}
            lowOutFlow: {self.lowOutFlow}
            outFlow: {self.outFlow}
            highOutFlow: {self.highOutFlow}
            stopHighRt: {self.stopHighRt}
            highRt: {self.highRt}
            normalRt: {self.normalRt}
            lowRt: {self.lowRt}
            stopLowRt: {self.stopLowRt}
        )
        '''
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str  # it can be Susv1, Susv2, etc.
    ) -> 'Susv':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @abstractmethod
    def provide_flows(self, *args, **kwargs) -> None:
        pass

        return None
