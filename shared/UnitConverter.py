from enum import Enum


class UnitConverter(Enum):
    MPS_TO_LPH: float = 3600 / 1000  # convert ml/s to L/h
    HOURS_TO_DAYS: float = 1 / 24  # days/hours
    HOURS_TO_MINUTES: float = 60  # minutes/hours
    LITERS_TO_MILLILITERS: float = 1000  # convert L to ml or cm3
    MILLILITERS_TO_LITERS: float = 1 / 1000  # convert ml to L or cm3
    MINUTES_TO_DAYS: float = 1 / 1440  # days/minutes
