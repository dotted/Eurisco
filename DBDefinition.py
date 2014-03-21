__author__ = 'Nicolai'

# DBDefinition.py
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from Constants import connection_string

engine = create_engine(connection_string, echo=True)
Base = declarative_base()

########################################################################
class FlexPriceInfo(Base):
    """"""
    __tablename__ = "flex_price_info"

    id = Column(Integer, primary_key=True)
    price = Column(Float(asdecimal=True))
    currency = Column(String)
    timestamp = Column(Integer)
    unit = Column(Integer)

    #----------------------------------------------------------------------
    def __init__(self, price, currency, timestamp, unit):
        """"""
        self.price = price
        self.currency = currency
        self.timestamp = timestamp
        self.unit = unit

# create tables
Base.metadata.create_all(engine)
