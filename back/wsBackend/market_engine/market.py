import math
import random

stocks = [
    {'symbol': 'GM', 'open': 38.87},
    {'symbol': 'GE', 'open': 25.40},
    {'symbol': 'MCD', 'open': 97.05},
    {'symbol': 'UAL', 'open': 69.45},
    {'symbol': 'WMT', 'open': 83.24},
    {'symbol': 'AAL', 'open': 55.76},
    {'symbol': 'LLY', 'open': 76.12},
    {'symbol': 'JPM', 'open': 61.75},
    {'symbol': 'BAC', 'open': 15.84},
    {'symbol': 'BA', 'open': 154.50}
]

for stock in stocks:
    stock['last'] = stock['open']
    stock['high'] = stock['open']
    stock['low'] = stock['open']


def simulate_market(stock_input=None):
    if stock_input:
        stock = next((item for item in stocks if item["symbol"] == stock_input))
    else:
        index = math.floor(random.uniform(0.0, 1.0) * len(stocks))
        stock = stocks[index]
    max_change = stock['open'] * 0.005
    change = max_change - random.uniform(0.0, 1.0) * max_change * 2
    change = round(change * 100) / 100
    change = 0.01 if change == 0 else change
    last = stock['last'] + change

    if last > stock['open'] * 1.15 or last < stock['open'] * 0.85:
        change = -change
        last = stock['last'] + change

    stock['change'] = change
    stock['last'] = round(last * 100) / 100;
    if stock['last'] > stock['high']:
        stock['high'] = stock['last']
    if stock['last'] < stock['low']:
        stock['low'] = stock['last']
    return stock


class RandomMarket:

    def __init__(self):
        self.price = 100.0

    def update_market(self, volatility=0.2):
        change_percent = 2 * volatility * random.uniform(0.0, 1.0)
        if change_percent > volatility:
            change_percent -= (2 * volatility)
        change_amount = self.price * change_percent
        new_price = self.price + change_amount
        self.price = new_price
        return new_price
