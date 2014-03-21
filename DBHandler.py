__author__ = 'Nicolai'

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DBDefinition import FlexPriceInfo
from Constants import connection_string


class DBHandler():

  def __init__(self):
    # create engine
    engine = create_engine(connection_string, echo=True)
    # create a Session
    sessionMaker = sessionmaker(bind=engine)
    self.session = sessionMaker()

  def insertFlexInfo(self, price, currency, timestamp, unit):
    # Check if a timestamp already is present
    res = self.session.query(FlexPriceInfo).filter(FlexPriceInfo.timestamp == timestamp).first()
    # Insert flex price info if not already present.
    if res is None:
      new_flex_price_info = FlexPriceInfo(price, currency, timestamp, unit)
      self.session.add(new_flex_price_info)
      self.session.commit()

  def getFlexInfo(self):
    raise NotImplemented

  def updateFlexInfo(self):
    raise NotImplemented

  def deleteFlexInfo(self):
    raise NotImplemented

