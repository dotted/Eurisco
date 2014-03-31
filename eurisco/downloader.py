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


class Downloader:

    def __init__(self,
                 device_id,
                 meter_id=None,
                 type_id=None,
                 timestamp = datetime.now().isoformat(),
                 duration = None,
                 url = constants.default_eurisco_url):
        self.device_id = device_id
        self.meter_id = meter_id
        self.type_id = type_id
        self.timestamp = timestamp
        self.duration = duration
        self.url = url

    def get_flex_price(self):

        # Create our client object
        client = Client(self.url)
        #print(client)

        #Create the requestId object
        request_id = client.factory.create('requestId')
        request_id.meterId = self.meter_id
        request_id.deviceId = self.device_id

        # Request GetFlexPrice from the web service
        return client.service.GetFlexPrice(request_id,
                                           self.type_id,
                                           self.timestamp,
                                           self.duration)

if __name__ == '__main__':

    e = Downloader("1013", type_id=1)
    print(e.get_flex_price())
