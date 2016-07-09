'''
Filename        : stock_utils.py
Author          : Aditya Murray
Date            : 9th July 2016
Description     : Frequently used general constants and methods.
'''

import datetime
from pymongo import MongoClient

#TODO FTSE, JAPAN, CHINA, SENSEX, HONGKONG, TOKYO, GERMAN, FRENCH
#How each one is affected by other markets

#Database Information
client = MongoClient('mongodb://localhost:27017')
db = client['Stocks']

#Symbol ticker list csvs
CSV_URL_LIST={
        'AMEX' :
        'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download',
        'NYSE' :
        'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download',
        'NASDAQ' :
        'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download',
        'TSX' :
        'http://web.tmxmoney.com/constituents_data.php?index=^TSX&index_name=S%26P%2FTSX+Composite+Index'
        }

#Need the official name for the syntax of the csvs downloaded
US_STYLE_INDICES = ['AMEX', 'NYSE', 'NASDAQ']

US_CSV_FIELDNAMES = ("Symbol", "Name", "LastSale", "MarketCap", "ADR TSO",
                            "IPOyear", "Sector", "Industry", "Summary Quote")

TORONTO_CSV_FIELDNAMES = ('Name', 'Symbol')

TODAY = datetime.date.today()

