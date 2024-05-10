import copy
from typing import Literal
from equipment.Equipment import Equipment
from process_support.chrom_step.ProaBufferChromStep import ProaBufferChromStep
from process_support.chrom_step.ChromStep import ChromStep
from process_support.chrom_step.ProaLoadChromStep import ProaLoadChromStep
from process_support.column.ProaSbmColumn import ProaSbmColumn
from process_support.resin.ProaChromResin import ProaChromResin

#########################################################################################################
# CLASS
#########################################################################################################


class Proa(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        column: ProaSbmColumn,
        resin: ProaChromResin,
        steps: list[ChromStep],
        efficiency: float,
    ) -> None:

        self.column = column
        self.resin = resin
        self.steps = steps
        self.efficiency = efficiency  # in %

        self.numOfCycles: int = 0
        self.inFlow: float = 0

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, dict[str, str | float | int]],
        key: Literal['Proa', 'proa'] = 'Proa'
    ) -> 'Proa':
        '''
        Overloading the from_dictfile method to handle the Proa class.
        Proa class needs to duplicate the Loading steps to account for high, normal, and low flows.
        '''

        data = data[key]
        # Here, instantiate the necessary components
        resin = ProaChromResin(**data['resin'])
        column = ProaSbmColumn(**data['column'])

        # Process steps and duplicate specific ones
        steps = []
        for step_data in data['steps']:
            step = (ProaLoadChromStep if step_data['name'] == 'Loading' else ProaBufferChromStep)(
                **step_data)
            steps.append(step)
            # Duplicate Loading steps
            if step_data['name'] == 'Loading':
                # Use deepcopy to duplicate the step
                steps.append(copy.deepcopy(step))
                steps.append(copy.deepcopy(step))

        efficiency = data['efficiency']

        # Instantiate and return a new Proa object with the processed data
        return cls(column, resin, steps, efficiency)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def provide_flows(self, inflow: float) -> None:
        self.inFlow = inflow

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def calculate_steps(self, titer: float, flowPercentCompensation: float) -> None:
        # Instantiate the buffer steps
        buffer_steps = [step for step in self.steps if step.name !=
                        'Loading' and isinstance(step, ProaBufferChromStep)]

        for step in buffer_steps:
            step.calc_params(
                columnVol=self.column.volume,
                colInnerDiam=self.column.innerDiam,
            )

        # Instantiate the loading steps
        loading_steps = [step for step in self.steps if step.name ==
                         'Loading' and isinstance(step, ProaLoadChromStep)]
        load_flow_types = ['low', 'normal', 'high']
        load_flows = [self.inFlow * (1 + flowPercentCompensation / 100),
                      self.inFlow,
                      self.inFlow, self.inFlow * (1 - flowPercentCompensation / 100)]

        for i, step in enumerate(loading_steps):
            step.calc_params(
                inflow=load_flows[i],
                flowType=load_flow_types[i],
                columnVol=self.column.volume,
                colInnerDiam=self.column.innerDiam,
                targetLoad=self.resin.targetLoad,
                titer=titer
            )

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}(
            column={self.column},
            resin={self.resin},
            steps={self.steps},
            efficiency={self.efficiency},
            numOfCycles={self.numOfCycles},
            inFlow={self.inFlow}
        )
        '''
