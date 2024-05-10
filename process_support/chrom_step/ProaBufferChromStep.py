import math
from process_support.chrom_step.ChromStep import ChromStep
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class ProaBufferChromStep(ChromStep):
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

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self):
        return super().__str__()
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

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
