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

    def __str__(self):
        return (f"{self.__class__.__name__}(name={self.name}, cost={self.cost}, "
                f"targetLoad={self.targetLoad}, maxLoad={self.maxLoad})")


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

    def __str__(self):
        prime_load = self.primeLoad if self.primeLoad is not None else "N/A"
        return (f"{self.__class__.__name__}(name={self.name}, cost={self.cost}, "
                f"targetLoad={self.targetLoad}, maxLoad={self.maxLoad}, primeLoad={prime_load})")
