from ChromResin import ProaChromResin
from ChromStep import ChromStep
from Column import ProaSbmColumn


class Proa():

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

    def provide_flow(self, inflow: float, flowPercentCompensation: float) -> None:
        self.inFlow = inflow
        self.flowPercentCompensation = flowPercentCompensation

        return None
