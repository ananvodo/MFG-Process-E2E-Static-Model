#########################################################################################################
# CLASS
#########################################################################################################


from process_support.resin.ChromResin import ChromResin


class ProaChromResin(ChromResin):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        name: str,
        cost: float,
        targetLoad: float,
        maxLoad: float,
        primeLoad: float | None = None,
    ) -> None:

        super().__init__(
            name=name,
            cost=cost,
            targetLoad=targetLoad,
            maxLoad=maxLoad,
        )
        self.primeLoad = primeLoad

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def __str__(self):
        primeLoad = self.primeLoad if self.primeLoad is not None else "N/A"
        return f'''{super().__str__()},
            primeLoad: {primeLoad}
        )
        '''
