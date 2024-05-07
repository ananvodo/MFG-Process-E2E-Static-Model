from enum import Enum


class UnitConverter(Enum):
    MPS_TO_LPH: float = 3600 / 1000  # convert ml/s to L/h
