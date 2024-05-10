from typing import Literal
from equipment.guard_filter.GuardFilter import GuardFilter

#########################################################################################################
# CLASS
#########################################################################################################


class ProaGuardFilter(GuardFilter):
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------
    def __init__(
        self,
        type: str,
        partNumber: str,
        area: float,
        quantity: int,
        loading: float,
        flowPercentCompensation: float
    ) -> None:

        super().__init__(
            type=type,
            partNumber=partNumber,
            area=area,
            quantity=quantity,
            loading=loading,
            flowPercentCompensation=flowPercentCompensation
        )

        return None
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    @classmethod
    def from_dictfile(
        cls,
        data: dict[str, str | float | int],
        key: Literal['ProaGuardFilter', 'proaGuarFilter'] = 'ProaGuardFilter'
    ) -> 'ProaGuardFilter':

        return super().from_dictfile(data, key)
    # -------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------

    def provide_flows(self, inflow: float) -> None:
        super().provide_flows(inflow)

        return None
