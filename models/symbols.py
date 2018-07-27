class Symbol:
    def __init__(self, symbol=None, company=None, opening_price=0, trade_index=None, date_public=None):
        self.symbol = symbol
        self.company = company
        self.opening_price = opening_price
        self.trade_index = trade_index
        self.date_public = date_public

