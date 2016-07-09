'''
Filename        : stocks.py
Author          : Aditya Murray
Date            : 5th July 2016
Description     : Get a list of all the stock symbols.
'''

import os
import wget
import csv
import json
import datetime
import os.path

AMEX = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download'
NYSE = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download'
NASDAQ = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'

CSV_FIELDNAMES = ("Symbol", "Name", "LastSale", "MarketCap", "ADR TSO",
                    "IPOyear", "Sector", "Industry", "Summary Quote")

class Stocks:
    '''
    Get and classify the entire list
    '''
    def __init__(self):
        daily_timestamp = datetime.date.today()
        if not os.path.isfile('%s_amex.json'%daily_timestamp):
            self.amex_list = self.get_amex_list()
        if not os.path.isfile('%s_nyse.json'%daily_timestamp):
            self.nyse_list = self.get_nyse_list()
        if not os.path.isfile('%s_nasdaq.json'%daily_timestamp):
            self.nasdaq_list = self.get_nasdaq_list()

    def get_amex_list(self):
        wget.download(AMEX)
        amex_csv = open('companylist.csv', 'rb')
        amex_csv_list = amex_csv.readlines()[1:]
        open('companylist.csv', 'wb').writelines(amex_csv_list)
        with open('companylist.csv', 'rb') as amex_csv:
            reader = csv.DictReader(amex_csv, CSV_FIELDNAMES)
            timestamp = datetime.date.today()
            out = json.dumps([ row for row in reader ], indent=4, sort_keys=True)
            with open('%s_amex.json' %timestamp, 'wb') as amex_json:
                amex_json.write(out)
        os.system('rm companylist.csv')
        return out

    def get_nyse_list(self):
        wget.download(NYSE)
        nyse_csv = open('companylist.csv', 'rb')
        nyse_csv_list = nyse_csv.readlines()[1:]
        timestamp = datetime.date.today()
        open('companylist.csv', 'wb').writelines(nyse_csv_list)
        with open('companylist.csv', 'rb') as nyse_csv:
            reader = csv.DictReader(nyse_csv, CSV_FIELDNAMES)
            timestamp = datetime.date.today()
            out = json.dumps([ row for row in reader], indent=4, sort_keys=True)
            with open('%s_nyse.json'%timestamp, 'wb') as nyse_json:
                nyse_json.write(out)
        os.system('rm companylist.csv')
        return out


    def get_nasdaq_list(self):
        wget.download(NASDAQ)
        nasdaq_csv = open('companylist.csv', 'rb')
        nasdaq_csv_list = nasdaq_csv.readlines()[1:]
        open('companylist.csv', 'wb').writelines(nasdaq_csv_list)
        with open('companylist.csv', 'rb') as nasdaq_csv:
            reader = csv.DictReader(nasdaq_csv, CSV_FIELDNAMES)
            timestamp = datetime.date.today()
            out = json.dumps([row for row in reader], indent=4, sort_keys=True)
            with open('%s_nasdaq.json'%timestamp, 'wb') as nasdaq_json:
                nasdaq_json.write(out)
        os.system('rm companylist.csv')
        return out


class Stock:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


if __name__ == '__main__':
    stocks = Stocks()
