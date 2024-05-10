from abc import abstractmethod
from typing import Literal
from equipment.Equipment import Equipment
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class GuardFilter(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        type: str,
        partNumber: str,
        area: float,
        quantity: int,
        loading: float,
        flowPercentCompensation: float
    ) -> None:

        # -------------------------------------
        # User defined attributes
        # -------------------------------------
        # Filter design parameters
        self.type = type  # This is the type of filter
        self.partNumber = partNumber  # This is the part number of the filter
        self.area = area  # in m^2
        self.quantity = quantity  # This is the number of filters in the system
        self.loading = loading  # Volume loaded in the filter in L/m^2
        self.flowPercentCompensation = flowPercentCompensation  # in %

        self.totalArea = self.quantity * self.area  # m^2
        self.processVolume = self.totalArea * self.loading

        # -------------------------------------
        # Calculated attributes
        # -------------------------------------
        # Flows
        self.inFlow: float = 0  # L/h
        self.outFlow: float = 0  # L/h
        self.normalFlux: float = 0  # L/m^2/h
        self.lowFlux: float = 0  # L/m^2/h
        self.hihgFlux: float = 0  # L/m^2/h
        self.processTime: float = 0  # h
        self.changeoutTime: float = 0  # days

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}(
            type: {self.type}
            partNumber: {self.partNumber}
            area: {self.area}
            quantity: {self.quantity}
            loading: {self.loading}
            flowPercentCompensation: {self.flowPercentCompensation}
            totalArea: {self.totalArea}
            processVolume: {self.processVolume}
            inFlow: {self.inFlow}
            outFlow: {self.outFlow}
            normalFlux: {self.normalFlux}
            lowFlux: {self.lowFlux}
            hihgFlux: {self.hihgFlux}
            processTime: {self.processTime}
            changeoutTime: {self.changeoutTime}
        )
        '''
    # -------------------------------------------------------------------------------------------------

    def provide_flows(self, inflow: float) -> None:
        self.inFlow = inflow
        self.outFlow = inflow

        self.normalFlux = self.inFlow / self.area  # L/m^2/h
        self.lowFlux = self.normalFlux * \
            (1 - self.flowPercentCompensation / 100)  # L/m^2/h
        self.hihgFlux = self.normalFlux * \
            (1 + self.flowPercentCompensation / 100)  # L/m^2/h

        self.processTime = self.processVolume / self.inFlow  # h
        self.changeoutTime = self.processTime * Convert.HOURS_TO_DAYS.value  # days

        return None
