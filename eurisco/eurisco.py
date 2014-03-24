#!/usr/bin/env python
"""Downloads power price data from Eurisco's servers
"""
from __future__ import print_function
from doctest import debug
from datetime import datetime

import constants

from suds.client import Client
import pytz

__author__ = 'Nicolai Steffensen, Rene Jacobsen, and Bo Fjord Jensen'
__copyright__ = "Copyright 2014, Vi tre her"
__license__ = "All rights reserved"
__version__ = "0.0.1"
__status__ = "Prototype"


class Eurisco:

    def __init__(self,
                 device_id,
                 meter_id=None,
                 url=constants.default_eurisco_url):
        self.device_id = device_id
        self.meter_id = meter_id
        self.type_id = None
        self.date = None
        self.duration = None

    def __fetch_data(self, type, duration):

        # Create our client object
        client = Client(Eurisco.url)
        #print(client)

        #Create the requestId object
        request_id = client.factory.create('requestId')
        request_id.meterId = self.meter_id
        request_id.deviceId = self.device_id

        # Get current time in ISO 8601 format
        date = datetime.now().isoformat()

        # Request GetFlexPrice from the web service
        return client.service.GetFlexPrice(requestId, type, date, duration)

    def getCurrentPrice(self):
        """This methoid will return a dictionary with price, currency,
        date, units.
        @return dictionary with price, currency, data, units
        @rtype dict
        """
        flexInfo = {}
        price = 0
        result = self.__fetch_data(1, 300)
        for flexPriceSignal in result:
        #print(flexPriceSignal)
            for x in flexPriceSignal:
                if x[0] == 'entries':
                    for entry in x:
                        if isinstance(entry, str):
                            continue
                        flexInfo['price'] = entry[0]['value']
                        flexInfo['datetime'] = (entry[0]['startingTime'] -
                                                datetime.datetime(1970,
                                                                  1,
                                                                  1,
                                                                  tzinfo=pytz.utc)).total_seconds()
                elif x[0] == 'signalType':
                    for entry in x:
                        if isinstance(entry, str):
                            continue
                        flexInfo['unit'] = entry['perUnit']
                        flexInfo['currency'] = entry['currency']

        return flexInfo


if __name__ == '__main__':

    e = EuriscoData("1013", "1013")
    print(e.getCurrentPrice())
