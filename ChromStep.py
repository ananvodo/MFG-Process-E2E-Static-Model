from abc import ABC, abstractmethod
import math

from UnitConverter import UnitConverter as Convert


class ChromStep(ABC):

    def __init__(
        self,
        name: str,
        linearVel: float | None,
        bufferName: str,
        bufferCost: float,
        cvs: float | None,
        holdTime: float | None = None,
    ) -> None:

        # -------------------------------------
        # User defined attributes
        # -------------------------------------
        # Design parameters
        self.name = name  # Name of the step
        self.linearVel = linearVel  # in cm/h
        self.bufferName = bufferName  # Name of the buffer
        self.bufferCost = bufferCost  # in USD/L
        self.cvs = cvs
        self.holdTime = holdTime  # in minutes

        # -------------------------------------
        # Calculated attributes
        # -------------------------------------
        self.rt: float = 0  # in minutes
        self.flow: float = 0  # in L/h
        self.time: float = 0  # in minutes/cycle
        self.volume: float = 0  # in L/cycle. Buffer or load volume

        return None

    @abstractmethod
    def calc_params(self, ):

        return None


class LoadStep(ChromStep):

    def __init__(
        self,
        name: str,
        linearVel: float | None,
        bufferName: str,
        bufferCost: float,
        cvs: float | None,
        holdTime: float | None = None,
    ) -> None:

        super().__init__(
            name=name,
            linearVel=linearVel,
            bufferName=bufferName,
            bufferCost=bufferCost,
            cvs=cvs,
            holdTime=holdTime,
        )

        self.cvs: float = 0  # cvs for load must be calculated

        self.lowFlow: float = 0  # in L/h
        self.hihgFlow: float = 0  # in L/h

        self.lowFlowLinearVel: float = 0  # cm/h. LV at low flow
        self.linearVel = 0  # cm/h. LV at normal flow
        self.highFlowLinearVel: float = 0  # cm /h. LV at high flow

        self.lowFlowRt: float = 0  # min. RT at low flow
        self.highflowRt: float = 0  # min. RT at high flow

        self.lowFlowTime: float = 0  # min. Step time at low flow
        self.time: float = 0  # min. Step time at normal flow
        self.highFlowTime: float = 0  # min. Step time at high flow

        self.loadMass: float = 0  # in g

        return None

    def calc_params(
        self,
        inflow: float,  # in L/h
        flowPercentCompensation: float,  # in percentage
        columnVol: float,  # in liters
        colInnerDiam: float,  # in cm
        targetLoad: float,  # in g/L
        titer: float,  # in g/L
    ) -> None:

        self.lowFlow = inflow * (1 - flowPercentCompensation)
        self.flow = inflow
        self.hihgFlow = inflow * (1 + flowPercentCompensation)

        self.lowFlowLinearVel = self.lowFlow * Convert.LITERS_TO_MILLILITERS.value / \
            (math.pi * ((colInnerDiam / 2) ** 2))
        self.linearVel = self.flow * Convert.LITERS_TO_MILLILITERS.value / \
            (math.pi * ((colInnerDiam / 2) ** 2))
        self.highFlowLinearVel = self.hihgFlow * Convert.LITERS_TO_MILLILITERS.value / \
            (math.pi * ((colInnerDiam / 2) ** 2))

        self.lowFlowRt = (columnVol / self.lowFlow) * \
            Convert.HOURS_TO_MINUTES.value
        self.rt = (columnVol / self.flow) * Convert.HOURS_TO_MINUTES.value
        self.highflowRt = (columnVol / self.hihgFlow) * \
            Convert.HOURS_TO_MINUTES.value

        self.lowFlowTime = (targetLoad * columnVol) / \
            (self.lowFlow * titer) * Convert.HOURS_TO_MINUTES.value
        self.time = (targetLoad * columnVol) / (self.flow *
                                                titer) * Convert.HOURS_TO_MINUTES.value
        self.highFlowTime = (targetLoad * columnVol) / \
            (self.hihgFlow * titer) * Convert.HOURS_TO_MINUTES.value

        self.loadMass = columnVol * targetLoad  # in g
        self.volume = self.loadMass / titer  # in L
        self.cvs = self.volume / columnVol

        return None


class BufferStep(ChromStep):

    def __init__(
        self,
        name: str,
        linearVel: float | None,
        bufferName: str,
        bufferCost: float,
        cvs: float | None,
        holdTime: float | None = None,
    ) -> None:

        super().__init__(
            name=name,
            linearVel=linearVel,
            bufferName=bufferName,
            bufferCost=bufferCost,
            cvs=cvs,
            holdTime=holdTime,
        )

        return None

    def calc_params(
        self,
        columnVol: float,  # in liters
        colInnerDiam: float,  # in cm
    ) -> None:

        self.flow = self.linearVel * math.pi * \
            ((colInnerDiam / 2) ** 2) * Convert.MILLILITERS_TO_LITERS.value
        self.rt = (columnVol / self.flow) * Convert.HOURS_TO_MINUTES.value
        self.time = columnVol * self.cvs / self.flow * Convert.HOURS_TO_MINUTES.value
        self.volume = columnVol * self.cvs  # in L/cycle

        return None
