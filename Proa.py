from ChromResin import ProaChromResin
from ChromStep import ChromStep
from Column import ProaSbmColumn
from Equipment import Equipment


class Proa(Equipment):

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
        self.flowPercentCompensation: float = 0

        return None

    def provide_flows(self, inflow: float, flowPercentCompensation: float) -> None:
        self.inFlow = inflow
        self.flowPercentCompensation = flowPercentCompensation

        return None

    def calculate_steps(self, titer: float) -> None:
        for step in self.steps:

            if step.name in ('Loading', 'Load', 'loading', 'load'):
                step.calc_params(
                    self.inFlow,
                    self.flowPercentCompensation,
                    self.column.volume,
                    self.column.innerDiam,
                    self.resin.targetLoad,
                    titer
                )

            else:
                step.calc_params(
                    self.column.volume,
                    self.column.innerDiam,
                )

        return None
