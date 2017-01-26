'''
Filename        : stocks.py
Author          : Aditya Murray
Date            : 9th July 2016
Description     : Manage stocks, and collect information regarding each.
'''

import json
import ystockquote
import concurrent.futures
import googlefinance
from yahoo_finance import Share
from stock_utils import *
from googlefinance import getQuotes
from pprint import pprint
from colours import *

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
            '''collection = db['NASDAQSymbols']
            cursor = collection.find()
            #print cursor[0]
            element = cursor[0]
            sym =  element['symbol_info']['Symbol']
            sym = 'AAPL'
            for each in cursor:
               sym = each['symbol_info']['Symbol']
                print sym
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
                #    print '\nSymbols :  %s\n' %document['symbol_info']'''
            print self.get_nasdaq_data()

        def get_nasdaq_data(self):
            result = ''
            collection = db['NASDAQSymbols']
            cursor = collection.find()
            #print cursor[0]
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
                result = (executor.map(self.getstockinfo, cursor))
            return result

        def getstockinfo(self, sym):
            #List of json objects obtained
            json_objs = {}
            sym = sym['symbol_info']['Symbol'].strip()
            print 'SYMBOL NAME : %s'%sym
            #print holi_hai('\n====================YSTOCK======================\n')

            price = ystockquote.get_price(sym)
            json_objs['Ystock_Price'] = price

            historical_price = ystockquote.get_historical_prices(sym, '2016-01-01', '2016-01-5')
            json_objs['Ystock_HistoricalPrice'] = historical_price

            all_point = ystockquote.get_all(sym)
            json_objs['Ystock_ALL'] = all_point

            #Yahoo-finance
            #print holi_hai('\n==============YAHOO FINANCE====================\n')
            s = Share(sym)

            opening_price = s.get_open()
            json_objs['Yahoo_opening_price'] = opening_price

            yahoo_price = s.get_price()
            json_objs['Yahoo_price'] = s.get_price()

            yahoo_trade_time = s.get_trade_datetime()
            json_objs['Yahoo_get_trade_datetime'] = yahoo_trade_time

            yahoo_historical = s.get_historical('2016-01-01', '2016-01-5')
            json_objs['Yahoo_historical'] = yahoo_historical

            yahoo_info = s.get_info
            json_objs['Yahoo_info'] =  yahoo_info

            #Google finance
            #print holi_hai('\n============GOOGLE FINANCE=====================\n')

            google_quotes = getQuotes(sym)
            json_objs['Google_quotes'] = google_quotes

            google_quotes_vie = getQuotes([sym, 'VIE:BKS'])
            json_objs['Google_quotes_vie'] = google_quotes_vie

            #for document in cursor:
            #    print '\nSymbols : %s\n'  %document['symbol_info']
            return json_objs

if __name__ == '__main__':
    Stock()
