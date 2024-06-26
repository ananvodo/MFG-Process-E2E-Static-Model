from process_params.Params import Params

#########################################################################################################
# CLASS
#########################################################################################################


class ChromResinParams(Params):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        name: str,
        cost: float,
        targetLoad: float,
        maxLoad: float,
    ) -> None:

        self.name = name
        self.cost = cost
        self.targetLoad = targetLoad
        self.maxLoad = maxLoad

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: str = 'resin'
    ) -> 'ChromResinParams':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self):
        return f'''
        {self.__class__.__name__}:
            name: {self.name}
            cost: {self.cost}
            targetLoad: {self.targetLoad}
            maxLoad: {self.maxLoad}'''
