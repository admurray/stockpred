'''
Filename        : stocks.py
Author          : Aditya Murray
Date            : 9th July 2016
Description     : Manage stocks, and collect information regarding each.
'''

import json
import ystockquote
import googlefinance
from yahoo_finance import Share
from stock_utils import *
from googlefinance import getQuotes
from pprint import pprint

db_info = client['Amex']
db = client['Symbols']

collections = ['AMEXSymbols', 'NYSESymbols', 'NASDAQSymbols', 'TSXSymbols']

#TODO - yahoo finance also provides currency, could play around with that too.


class Stock:
        '''
        This module works on independent stocks and stores information about
        them
        '''
        def __init__(self):
            collection = db['AMEXSymbols']
            cursor = collection.find()
            #print cursor[0]
            element = cursor[0]
            sym =  element['symbol_info']['Symbol']
            #ystockquote
            print 'SYMBOL NAME : %s'%sym
            print '\n====================YSTOCK======================\n'
            print 'Price :  %s' %ystockquote.get_price(sym)
            pprint(ystockquote.get_historical_prices(sym, '2016-01-01',
                '2016-01-5'))
            pprint(ystockquote.get_all(sym))

            #Yahoo-finance
            print '\n==============YAHOO FINANCE====================\n'
            s = Share(sym)
            print 'Opening Price : %s'%s.get_open()
            print 'Price : %s' %s.get_price()
            print 'Trade Datetime : %s\n' %s.get_trade_datetime()
            pprint(s.get_historical('2016-01-01', '2016-01-5'))
            pprint(s.get_info)

            #Google finance
            print '\n============GOOGLE FINANCE=====================\n'
            print json.dumps(getQuotes(sym), indent=2)
            print '\n\ngetQuotes(\'%s\', \'VIE:BKS\')]\n' %sym
            print json.dumps(getQuotes([sym, 'VIE:BKS']), indent=2)

            #for document in cursor:
            #    print '\nSymbols :  %s\n' %document['symbol_info']


if __name__ == '__main__':
    Stock()
