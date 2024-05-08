class ChromResin():

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


class ProaChromResin(ChromResin):

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
