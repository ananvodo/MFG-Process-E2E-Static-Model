from process_params.Params import Params

#########################################################################################################
# CLASS
#########################################################################################################


class ChromStepParams(Params):
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

        self.name = name  # Name of the step
        self.linearVel = linearVel  # in cm/h
        self.bufferName = bufferName  # Name of the buffer
        self.bufferCost = bufferCost  # in USD/L
        self.cvs = cvs
        self.holdTime = holdTime  # in minutes

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str = 'steps'
    ) -> 'ChromStepParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'''
        {self.__class__.__name__}:
            name: {self.name}
            linearVel: {self.linearVel}
            bufferName: {self.bufferName}
            bufferCost: {self.bufferCost}
            cvs: {self.cvs}
            holdTime: {self.holdTime}'''
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
