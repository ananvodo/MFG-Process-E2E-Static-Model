import math
from typing import Literal
from equipment.Equipment import Equipment
from equipment.SusvDiscr import SusvDiscr
from process_params.BioreactorParams import BioreactorParams
from process_params.DepthFilterParams import DepthFilterParams
from shared.UnitConverter import UnitConverter as Convert

#########################################################################################################
# CLASS
#########################################################################################################


class DepthFilterDiscr(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    class Process():
        def __init__(
            self,
            inFlow: float,
            outFlow: float,
            flux: float,
            processTime: float,
            changeoutTime: float,
            quantityPerRun: int,

            flowType: Literal['low', 'normal', 'high']
        ) -> None:

            self.inFlow = inFlow  # L/h
            self.outFlow = outFlow  # L/h
            self.flux = flux  # L/m^2/h
            self.processTime = processTime  # h
            self.changeoutTime = changeoutTime  # days
            self.changeoutTime = changeoutTime  # days
            self.quantityPerRun = quantityPerRun  # number of filters for the operation
            self.flowType = flowType  # Options: 'low', 'normal', 'high'

            return None

        def __str__(self) -> str:
            return f'''
            {self.__class__.__name__}:
                inFlow: {self.inFlow}
                outFlow: {self.outFlow}
                flux: {self.flux}
                processTime: {self.processTime}
                changeoutTime: {self.changeoutTime}
                quantityPerRun: {self.quantityPerRun}
                flowType: {self.flowType}'''

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        process: list[Process],
    ):
        self.process = process

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        depthFilterParams: DepthFilterParams,
        bioreactorParams: BioreactorParams,
        susvDiscr: SusvDiscr,
    ) -> 'DepthFilterDiscr':

        process = []

        for susv in susvDiscr.process:
            flowType = susv.flowType
            inFlow: float = susv.outFlow
            outFlow: float = susv.outFlow
            flux: float = outFlow / depthFilterParams.totalArea
            processTime: float = depthFilterParams.processVolume / outFlow
            changeoutTime: float = processTime * Convert.HOURS_TO_DAYS.value  # days
            quantityPerRun: int = math.ceil(
                bioreactorParams.prodDays / (changeoutTime * depthFilterParams.quantity))

            process.append(cls.Process(
                inFlow=inFlow,
                outFlow=outFlow,
                flux=flux,
                processTime=processTime,
                changeoutTime=changeoutTime,
                quantityPerRun=quantityPerRun,
                flowType=flowType
            ))

        # Create an instance of the class
        instance = cls(process)
        # Now you can call load_params on the instance
        instance.load_params(depthFilterParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        process_str = ",\n    ".join(str(step) for step in self.process)
        # Make sure all the attributes from the params are included
        type_ = getattr(self, 'type', None)
        partNumber = getattr(self, 'partNumber', None)
        area = getattr(self, 'area', None)
        quantityPerRun = getattr(self, 'quantityPerRun', None)
        loading = getattr(self, 'loading', None)
        bufferFlushLoading = getattr(self, 'bufferFlushLoading', None)
        bufferFlushFlux = getattr(self, 'bufferFlushFlux', None)
        totalArea = getattr(self, 'totalArea', None)
        bufferFlushVolume = getattr(self, 'bufferFlushVolume', None)
        bufferFlushTime = getattr(self, 'bufferFlushTime', None)
        processVolume = getattr(self, 'processVolume', None)

        return f'''
        {self.__class__.__name__}:
            type: {type_}
            partNumber: {partNumber}
            area: {area}
            quantityPerRun: {quantityPerRun}
            loading: {loading}
            bufferFlushLoading: {bufferFlushLoading}
            bufferFlushFlux: {bufferFlushFlux}
            totalArea: {totalArea}
            bufferFlushVolume: {bufferFlushVolume}
            bufferFlushTime: {bufferFlushTime}
            processVolume: {processVolume}
            process:[\n{process_str}\n           ]'''