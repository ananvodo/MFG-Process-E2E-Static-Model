from typing import Literal
from equipment.Equipment import Equipment
from equipment.SusvDiscr import SusvDiscr
from process_params.GuardFilterParams import GuardFilterParams
from shared.UnitConverter import UnitConverter as Convert


class GuardFilterDiscr(Equipment):
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
            flowType: Literal['low', 'normal', 'high']
        ) -> None:

            self.inFlow = inFlow  # L/h
            self.outFlow = outFlow  # L/h
            self.flux = flux  # L/m^2/h
            self.processTime = processTime  # h
            self.changeoutTime = changeoutTime  # days
            self.flowType = flowType  # Options: 'low', 'normal', 'high'

            return None

        def __str__(self) -> str:
            return f'''
            {self.__class__.__name__}:
                inFlow: {self.inFlow}
                outFlow: {self.outFlow}
                flux: {self.flux}
                flowType: {self.flowType}'''

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        process: Process
    ) -> None:

        self.process = process

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        guardFilterDiscrParams: GuardFilterParams,
        susvDiscr: SusvDiscr,
    ) -> 'GuardFilterDiscr':

        process = []

        for susv in susvDiscr.process:
            flowType = susv.flowType
            inFlow: float = susv.inFlow
            outFlow: float = susv.outFlow
            flux: float = outFlow / guardFilterDiscrParams.area
            processTime: float = guardFilterDiscrParams.processVolume / outFlow
            changeoutTime: float = processTime * Convert.HOURS_TO_DAYS.value  # days

            process.append(cls.Process(
                inFlow=inFlow,
                outFlow=outFlow,
                flux=flux,
                processTime=processTime,
                changeoutTime=changeoutTime,
                flowType=flowType
            ))

        # Create an instance of the class
        instance = cls(process)
        # Now you can call load_params on the instance
        instance.load_params(guardFilterDiscrParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        process_str = ",\n    ".join(str(step) for step in self.process)
        # Make sure all the attributes from the params are included
        type_ = getattr(self, 'type', None)
        partNumber = getattr(self, 'partNumber', None)
        area = getattr(self, 'area', None)
        quantity = getattr(self, 'quantity', None)
        loading = getattr(self, 'loading', None)
        totalArea = getattr(self, 'totalArea', None)
        processVolume = getattr(self, 'processVolume', None)

        return f'''
        {self.__class__.__name__}:
            type: {type_}
            partNumber: {partNumber}
            area: {area}
            quantity: {quantity}
            loading: {loading}
            totalArea: {totalArea}
            processVolume: {processVolume}
            process:[\n{process_str}\n           ]'''
