#!/usr/bin/env python
"""Collection of various datatypes used for Eurisco
"""
from enum import Enum

__author__ = 'Nicolai Steffensen, Rene Jacobsen, and Bo Fjord Jensen'
__copyright__ = "Copyright 2014, Vi tre her"
__license__ = "All rights reserved"
__version__ = "0.0.1"
__status__ = "Prototype"


class SignalPriceTypeType(Enum):
    RegulationPowerPrice = 1
    SpotPrice = 2
    DayAheadPrice = 2
    Prognosis = 2
    Forecast = 2
    NetPrice = 3


class SignalUncertaintyType(Enum):
    NoUncertainty = 0
    Prognosis = 1
    HighPrice = 2
    LowPrice = 3
    PercentageAbove = 4
    PercentageBelow = 5
    PercentageAboveAndBelow = 6
    Fractiles = 7


class PerUnitType(Enum):
    Wh = 1
    kWh = 2
    MWh = 3
    Index = 4
    Percentage = 4
