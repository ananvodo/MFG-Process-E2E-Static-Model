from process_support.column.Column import Column

#########################################################################################################
# CLASS
#########################################################################################################


class ProaSbmColumn(Column):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        innerDiam: float,
        bedHeight: float,
        quantity: int,
    ) -> None:

        super().__init__(
            innerDiam=innerDiam,
            bedHeight=bedHeight,
            quantity=quantity,
        )

        return None
