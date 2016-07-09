'''
Filename        : stocks.py
Author          : Aditya Murray
Date            : 5th July 2016
Description     : Database methods handling stock database
'''

import json
from pymongo import MongoClient
from stock_utils import *

class DBStocks:
    def update_stock_symbols(self):
        for each in US_STYLE_INDICES:
            print each
            db['%sSymbols' %each].remove({})
            collection = db['%sSymbols' %each]
            self.add_symbols(collection, each)

        db['TsxSymbols'].remove({})
        collection = db['TsxSymbols']
        self.add_tsx_symbols(collection)


    def add_symbols(self, collection, index):
        with open('%s_%s.json' %(TODAY, index)) as sym_file:
            data = json.load(sym_file)
            print len(data)
            collection.insert([{'x': i} for i in range(len(data))])
            print collection.inserted_ids
            #pprint(data)


    def add_tsx_symbols(self, collection):
        with open('%s_TSX.json'%TODAY) as sym_file:
            data = json.load(sym_file)
            print len(data)
            collection.insert([{'x': i} for i in range(len(data))])
            print collection.inserted_ids
            collection.count()
            #pprint(data)


