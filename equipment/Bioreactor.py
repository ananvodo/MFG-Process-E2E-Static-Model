from equipment.Equipment import Equipment
from process_params.BioreactorParams import BioreactorParams

#########################################################################################################
# CLASS
#########################################################################################################


class Bioreactor(Equipment):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        inFlow: float,
        outFlow: float,
        bleedFlow: float,
    ) -> None:

        self.inFlow = inFlow
        self.outFlow = outFlow
        self.bleedFlow = bleedFlow

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_params(
        cls,
        bioreactorParams: BioreactorParams,
    ) -> 'Bioreactor':

        outFlow: float = bioreactorParams.volume * bioreactorParams.vvd / 24
        inFlow: float = bioreactorParams.outFlow * \
            (1 + bioreactorParams.bleedPercent / 100)
        bleedFlow: float = bioreactorParams.outFlow * \
            (bioreactorParams.bleedPercent / 100)

        # Create an instance of the class
        instance = cls(inFlow, outFlow, bleedFlow)
        # Now you can call load_params on the instance
        instance.load_params(bioreactorParams)

        return instance

    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        # Making sure all the attributes from BioreactprParams are loaded
        prodDays = getattr(self, 'prodDays', None)
        titer = getattr(self, 'titer', None)
        volume = getattr(self, 'volume', None)
        vvd = getattr(self, 'vvd', None)
        bleedPercent = getattr(self, 'bleedPercent', None)

        return f'''
        {self.__class__.__name__}:
            prodDays: {prodDays}
            titer: {titer}
            volume: {volume}
            vvd: {vvd}
            bleedPercent: {bleedPercent}
            outFlow: {self.outFlow}
            inFlow: {self.inFlow}
            bleedFlow: {self.bleedFlow}
            inFlow = {self.inFlow},
            outFlow = {self.outFlow},
            bleedFlow = {self.bleedFlow}'''
