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
import json
from pprint import pprint
from db_stocks import DBStocks
from stock_utils import *


class Symbols:
    '''
    Get and classify the entire list
    '''
    def __init__(self):
        for each in US_STYLE_INDICES:
            if not os.path.isfile('%s_%s.json'%(TODAY, each)):
                self.get_us_symbol_list(each)

        if not os.path.isfile('%s_TSX.json'%TODAY):
            self.tsx_list = self.get_tsx_list()

        DBStocks().update_stock_symbols()

    def get_us_symbol_list(self, index):
        filename = wget.download(CSV_URL_LIST[index])
        csv_file = open(filename, 'rb')
        csv_list = csv_file.readlines()[1:]
        open(filename, 'wb').writelines(csv_list)
        with open(filename, 'rb') as csv_file:
            reader= csv.DictReader(csv_file, US_CSV_FIELDNAMES)
            out = json.dumps([ row for row in reader ], indent=4, sort_keys=True)
            with open('%s_%s.json' %(TODAY, index), 'wb') as json_file:
                json_file.write(out)
        os.system('rm %s' %filename)
        return out


    def get_tsx_list(self):
        filename = wget.download(CSV_URL_LIST['TSX'])
        tsx_csv = open(filename, 'rb')
        tsx_csv_list = tsx_csv.readlines()[5:]
        open(filename, 'wb').writelines(tsx_csv_list)
        with open(filename, 'rb') as tsx_csv:
            reader = csv.DictReader(tsx_csv, TORONTO_CSV_FIELDNAMES)
            out = json.dumps([row for row in reader], indent=4, sort_keys=True)
            with open('%s_TSX.json'%TODAY, 'wb') as tsx_json:
                tsx_json.write(out)
        os.system('rm %s' %filename)
        return out

if __name__ == '__main__':
    Symbols()
