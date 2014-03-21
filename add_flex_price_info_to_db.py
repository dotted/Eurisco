__author__ = 'Nicolai'

import DBHandler
import Eurisco


eurisco = Eurisco.EuriscoData("1013", "1013")
dbhandler = DBHandler.DBHandler()

data = eurisco.getCurrentPrice()
dbhandler.insertFlexInfo(data['price'], data['currency'], data['datetime'], data['unit'])

