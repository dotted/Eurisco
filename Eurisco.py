from __future__ import print_function
from doctest import debug
from suds.client import Client
import datetime
import pytz

__author__ = 'Nicolai'


class EuriscoData:

  url = "http://backend.eurisco.dk:4040/webservices/flexprice?wsdl"

  def  __init__(self, deviceId, meterId):
    self.deviceid = deviceId
    self.meterid = meterId
    self.typeid = None
    self.date = None
    self.duration = None


  def __fetch_data(self, type, duration):

    # Create our client object
    client = Client(self.url)
    #print(client)

    #Create the requestId object
    requestId = client.factory.create('requestId')
    requestId.meterId = self.meterid
    requestId.deviceId = self.deviceid

    # Get current time in ISO 8601 format
    date = datetime.datetime.now().isoformat()

    # Request GetFlexPrice from the web service
    return client.service.GetFlexPrice(requestId, type, date, duration)

  """
  This methoid will return a dictionary with price, currency,
  date, units.
  @return dictionary with price, currency, data, units
  @rtype dict
  """
  def getCurrentPrice(self):

    flexInfo = {}
    price = 0
    result = self.__fetch_data(1, 7200)
    for flexPriceSignal in result:
      #print(flexPriceSignal)
      for x in flexPriceSignal:
        if x[0] == 'entries':
          for entry in x:
            if isinstance(entry, str):
              continue
            flexInfo['price'] = entry[0]['value']
            flexInfo['datetime'] = (entry[0]['startingTime'] - datetime.datetime(1970,1,1,tzinfo=pytz.utc)).total_seconds()
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