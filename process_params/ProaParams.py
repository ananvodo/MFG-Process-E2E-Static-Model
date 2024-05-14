from process_params.ChromColumnParams import ChromColumnParams
from process_params.ChromResinParams import ChromResinParams
from process_params.ChromStepParams import ChromStepParams
from process_params.Params import Params

#########################################################################################################
# CLASS
#########################################################################################################


class ProaParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        column: ChromColumnParams,
        resin: ChromResinParams,
        steps: list[ChromStepParams],
        efficiency: float,
    ) -> None:

        self.column = column
        self.resin = resin
        self.steps = steps
        self.efficiency = efficiency  # in %

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, dict[str, str | float | int]],
        key: str = 'Proa'
    ) -> 'ProaParams':
        '''
        Overloading the from_dictfile method to handle the Proa class.
        Proa class needs to duplicate the Loading steps to account for high, normal, and low flows.
        '''

        data = data[key]
        # Here, instantiate the necessary components
        resin = ChromResinParams(**data['resin'])
        column = ChromColumnParams(**data['column'])
        efficiency = data['efficiency']

        # Process steps and duplicate specific ones
        steps = []
        for step_data in data['steps']:
            step = ChromStepParams(**step_data)
            steps.append(step)

        return cls(column, resin, steps, efficiency)

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        steps_str = ",\n    ".join(str(step) for step in self.steps)

        return f'''
        {self.__class__.__name__}:
            efficiency: {self.efficiency}
            column: {self.column}
            resin: {self.resin}
            steps: [\n{steps_str}\n          ]'''
