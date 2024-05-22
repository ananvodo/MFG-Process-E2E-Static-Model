from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Literal
from process_data.ProcessVariation import ProcessVariation
from process_params.GuardFilterParams import GuardFilterParams
from shared.UnitConverter import UnitConverter as Convert


class GuardFilterDiscr(ProcessVariation):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    class Process(ProcessVariation.Process):
        def __init__(
            self,
            inFlow: float,
            outFlow: float,
            flux: float,
            processTime: float,
            processVolume: float,
            changeoutTime: float,
            flowType: Literal['low', 'normal', 'high']
        ) -> None:

            self.inFlow = inFlow  # L/h
            self.outFlow = outFlow  # L/h
            self.flux = flux  # L/m^2/h
            self.processTime = processTime  # h
            self.processVolume = processVolume  # L
            self.changeoutTime = changeoutTime  # days
            self.flowType = flowType  # Options: 'low', 'normal', 'high'

            return None

        def __str__(self) -> str:
            return f'''
            {self.__class__.__name__}:
                inFlow: {self.inFlow}
                outFlow: {self.outFlow}
                flux: {self.flux}
                processVolume: {self.processVolume}
                processTime: {self.processTime}
                changeoutTime: {self.changeoutTime}
                flowType: {self.flowType}'''

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        titer: float,
        process: list[Process],
    ) -> None:

        self.titer = titer  # in g/L
        self.process = process

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @property
    def process(self) -> list[GuardFilterDiscr.Process]:
        return self._process

    @process.setter
    def process(self, value: list[GuardFilterDiscr.Process]) -> None:
        self._process = value
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        guardFilterDiscrParams: GuardFilterParams,
        prevEquipment: ProcessVariation,
    ) -> GuardFilterDiscr:

        process: list[cls.Process] = []

        for susv in prevEquipment.process:
            flowType = susv.flowType
            inFlow: float = susv.outFlow
            outFlow: float = susv.outFlow
            flux: float = outFlow / guardFilterDiscrParams.totalArea
            processTime: float = guardFilterDiscrParams.processVolume / outFlow
            processVolume: float = inFlow * processTime  # L
            changeoutTime: float = processTime * Convert.HOURS_TO_DAYS.value  # days

            process.append(cls.Process(
                inFlow=inFlow,
                outFlow=outFlow,
                flux=flux,
                processTime=processTime,
                processVolume=processVolume,
                changeoutTime=changeoutTime,
                flowType=flowType
            ))

        # Create an instance of the class
        instance = cls(process=process, titer=prevEquipment.titer)
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

        return f'''
        {self.__class__.__name__}:
            type: {type_}
            partNumber: {partNumber}
            area: {area}
            quantity: {quantity}
            loading: {loading}
            totalArea: {totalArea}
            process:[\n{process_str}\n           ]'''
