'''
Filename        : stocks.py
Author          : Aditya Murray
Date            : 5th July 2016
Description     : Database methods handling stock database
'''

import json
from pymongo import MongoClient
from stock_utils import *
from colours import *

class DBStocks:
    def update_stock_symbols(self):
        for each in US_STYLE_INDICES:
            print '%s %s' %('Updating symbol list for : ', bright_colour(each))
            db['%sSymbols' %each].remove({})
            collection = db['%sSymbols' %each]
            self.add_symbols(collection, each)

        print '%s %s' %('Updating symbol list for : ', bright_colour('TSX'))
        db['TsxSymbols'].remove({})
        collection = db['TsxSymbols']
        self.add_tsx_symbols(collection)


    def add_symbols(self, collection, index):
        with open('%s_%s.json' %(TODAY, index)) as sym_file:
            data = json.load(sym_file)
            collection.insert([{'x': i} for i in range(len(data))])
            print '%s %s' %('Total documents inserted : ' , bright_colour(len(data)))
            print '%s\n%s' %('Inserted collection id : ', bright_colour(collection.inserted_ids))
            #pprint(data)


    def add_tsx_symbols(self, collection):
        with open('%s_TSX.json'%TODAY) as sym_file:
            data = json.load(sym_file)
            collection.insert([{'x': i} for i in range(len(data))])
            print '%s %s' %('Total documents inserted : ' , bright_colour(len(data)))
            print '%s %s' %('Inserted collection id : ', bright_colour(collection.inserted_ids))
            #pprint(data)
