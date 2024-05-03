class Susv():

    def __init__(self, percentFlowComp: float, inflow: float, flowPercentCompensation: float,
                 stopHighAlarm: float, highAlarm: float, normalAlarm: float, lowAlarm: float,
                 stopLowAlarm: float, vesselVolume: float, phAdjustPercent: float,
                 conductivityAdjustPercent: float):
        self.percentFlowComp = percentFlowComp
        self.inFlow = inflow
        self.flowPercentCompensation = flowPercentCompensation
        self.stopHighAlarm = stopHighAlarm
        self.highAlarm = highAlarm
        self.normalAlarm = normalAlarm
        self.lowAlarm = lowAlarm
        self.stopLowAlarm = stopLowAlarm
        self.vesselVolume = vesselVolume
        self.phAdjustPercent = phAdjustPercent
        self.conductivityAdjustPercent = conductivityAdjustPercent

        return None


class ContinuousSusv(Susv):

    def __init__(self):
        super().__init__()

        return None

    def setOutFlow(self, outFlow: float):
        self.normalOutflow: float = outFlow
        self.lowOutFlow: float = self.normalOutflow * \
            (1 - self.flowPercentCompensation)
        self.highOutFlow: float = self.normalOutflow * \
            (1 + self.flowPercentCompensation)

        return None


class SemiContinuousSusv(Susv):

    def __init__(self):
        super().__init__()

        return None

    def setOutFlow(self):
        self.normalOutflow: float = self.inFlow * \
            (1 + self.phAdjustPercent / 100 + self.conductivityAdjustPercent / 100)
        self.lowOutFlow: float = self.normalOutflow * \
            (1 - self.flowPercentCompensation)
        self.highOutFlow: float = self.normalOutflow * \
            (1 + self.flowPercentCompensation)

        return None
