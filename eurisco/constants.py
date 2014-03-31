#!/usr/bin/env python

from datetime import datetime

import os

import pytz

__author__ = 'Nicolai Steffensen, Rene Jacobsen, and Bo Fjord Jensen'
__copyright__ = "Copyright 2014, Vi tre her"
__license__ = "All rights reserved"
__version__ = "0.0.1"
__status__ = "Prototype"

default_eurisco_url = "http://backend.eurisco.dk:4040/webservices/flexprice?wsdl"

#
epochtime = datetime(1970, 1, 1,tzinfo=pytz.utc)

# Database
flex_price_database_filename = 'FlexPriceInfo.db'
database = 'sqlite'
database_connection_string = database + ':///' + os.path.dirname(os.path.realpath(__file__)) + '/' + flex_price_database_filename
