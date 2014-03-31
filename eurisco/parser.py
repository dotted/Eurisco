#!/usr/bin/env python
"""Downloads power price data from Eurisco's servers
"""
from __future__ import print_function
from doctest import debug
from datetime import datetime
import constants

from datatypes import enumerations

from suds.client import Client
from moneyed.classes import Money
import pytz

__author__ = 'Nicolai Steffensen, Rene Jacobsen, and Bo Fjord Jensen'
__copyright__ = "Copyright 2014, Vi tre her"
__license__ = "All rights reserved"
__version__ = "0.0.1"
__status__ = "Prototype"


class Parser:

    def __init__(self,
                 flex_price):
        self.flex_price = flex_price

    def get_current_price(self):
        """This methoid will return a dictionary with price, currency,
        date, units.
        @return dictionary with price, currency, data, units
        @rtype dict
        """
        flexInfo = {}
        price = ""
        currency = ""
        result = self.flex_price.get_flex_price()
        for flexPriceSignal in result:
        #print(flexPriceSignal)
            for x in flexPriceSignal:
                if x[0] == 'entries':
                    for entry in x:
                        if isinstance(entry, str):
                            continue
                        price = entry[0]['value']
                        flexInfo['datetime'] = (entry[0]['startingTime'] -
                                                constants.epochtime).total_seconds()
                elif x[0] == 'signalType':
                    for entry in x:
                        if isinstance(entry, str):
                            continue
                        flexInfo['unit'] = enumerations.PerUnitType(int(entry['perUnit']))
                        currency = entry['currency']
        flexInfo['price'] = Money(amount = price, currency = currency)
        return flexInfo


if __name__ == '__main__':

    from downloader import Downloader
    d = Downloader("1013", type_id = 1)
    p = Parser(d)
    print(p.get_current_price())

