import math
from typing import Literal, Optional

from process_support.chrom_step.ChromStep import ChromStep
from shared.UnitConverter import UnitConverter as Convert
#########################################################################################################
# CLASS
#########################################################################################################


class ProaLoadChromStep(ChromStep):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
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
        self.flowType: Optional[Literal['low', 'normal', 'high']] = None
        self.cvs: float = 0  # cvs for load must be calculated
        self.linearVel = 0  # cm/h. LV at normal flow
        self.loadMass: float = 0  # in g
        self.flow: float = 0  # in L/h

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {super().__str__()},
            flowType={self.flowType},
            loadMass={self.loadMass}
        )
        '''
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def calc_params(
        self,
        inflow: float,  # in L/h
        flowType: Optional[Literal['low', 'normal', 'high']],
        columnVol: float,  # in liters
        colInnerDiam: float,  # in cm
        targetLoad: float,  # in g/L
        titer: float,  # in g/L
    ) -> None:

        self.flowType = flowType
        self.flow = inflow
        self.linearVel = self.flow * Convert.LITERS_TO_MILLILITERS.value / \
            (math.pi * ((colInnerDiam / 2) ** 2))
        self.rt = (columnVol / self.flow) * Convert.HOURS_TO_MINUTES.value
        self.time = (targetLoad * columnVol) / (self.flow *
                                                titer) * Convert.HOURS_TO_MINUTES.value
        self.loadMass = columnVol * targetLoad  # in g
        self.volume = self.loadMass / titer  # in L
        self.cvs = self.volume / columnVol

        return None
