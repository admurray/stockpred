'''
Filename        : stocks.py
Author          : Aditya Murray
Date            : 9th July 2016
Description     : Manage stocks, and collect information regarding each.
'''

import json
from stock_utils import *


db_info = client['Amex']
db = client['Symbols']

collections = ['AMEXSymbols', 'NYSESymbols', 'NASDAQSymbols', 'TSXSymbols']

class Stock:
        '''
        This module works on independent stocks and stores information about
        them
        '''
        def __init__(self):
            collection = db['AMEXSymbols']
            cursor = collection.find()
            for document in cursor:
                print document

if __name__ == '__main__':
    Stock()
