from equipment.BufferProaChromStep import BufferProaChromStep
from equipment.Equipment import Equipment
from equipment.LoadProaChromStep import LoadProaChromStep
from equipment.SusvDiscr import SusvDiscr
from process_params.BioreactorParams import BioreactorParams
from process_params.ChromParams import ChromParams

#########################################################################################################
# CLASS
#########################################################################################################


class Proa(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        steps: list[BufferProaChromStep | LoadProaChromStep],
        capturedMass: float,
        titer: float
    ) -> None:

        self.steps = steps
        self.capturedMass = capturedMass  # g/cycle
        self.titer = titer  # g/L per cycle

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    @classmethod
    def from_params(
        cls,
        chromParams: ChromParams,
    ) -> 'Proa':

        steps = []

        for step_params in chromParams.steps:

            if step_params.name not in ('Loading', 'loading', 'Load', 'load'):
                step = BufferProaChromStep.from_params(
                    chromColumnParams=chromParams.column,
                    chromStepParams=step_params
                )

            steps.append(step)

        elution_step = [step for step in steps if step.name in (
            'Elution', 'elution', 'Elute', 'elute')][0]

        capturedMass = chromParams.column.volume * \
            chromParams.resin.targetLoad * chromParams.efficiency / 100  # g
        titer = capturedMass / elution_step.volume  # g/L

        # Create an instance of the class
        instance = cls(steps=steps, titer=titer, capturedMass=capturedMass)
        # Now you can call load_params on the instance
        instance.load_params(chromParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def calculate_loading(
        self,
        proaParams: ChromParams,
        susvDiscr: SusvDiscr,
        bioreactorParams: BioreactorParams,
    ) -> 'Proa':

        for process in susvDiscr.process:

            for step_data in proaParams.steps:
                if isinstance(step_data, LoadProaChromStep):
                    if step_data.flowType == process.flowType:
                        raise ValueError('Flow type already calculated')

            for step_params in proaParams.steps:

                if step_params.name in ('Loading', 'loading', 'Load', 'load'):
                    step = LoadProaChromStep.from_params(
                        chromStepParams=step_params,
                        susvDiscrProcess=process,
                        chromColumnParams=proaParams.column,
                        bioreactorParams=bioreactorParams,
                        chromResinParams=proaParams.resin
                    )
                    self.steps.append(step)

        return None

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        steps_str = ",\n    ".join(str(step) for step in self.steps)
        # Making sure all the attributes from Equipment class are loaded
        efficiency = getattr(self, 'efficiency', None)
        column = getattr(self, 'column', None)
        resin = getattr(self, 'resin', None)

        return f'''{self.__class__.__name__}:
            efficiency: {efficiency}
            column: {column}
            resin: {resin}
            capturedMass: {self.capturedMass}
            titer: {self.titer}
            steps: [\n{steps_str}\n          ]'''
