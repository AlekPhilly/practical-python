# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    with open(filename) as file:
        rows = csv.reader(file)
        portfolio = []
        next(rows)
        for row in rows:
            holding = {
                'name': row[0], 
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    with open(filename) as file:
        rows = csv.reader(file)
        prices = {}
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Empty line')
                pass
    return prices

def make_report(stocks_list, prices_dict):
    report = []
    for holding in stocks_list:
        price = prices[holding['name']]
        change = price - holding['price']
        entry = (holding['name'], holding['shares'], price, change)
        report.append(entry)
    return report

portfolio_path = r'Data\portfolio.csv'
prices_path = r'Data\prices.csv'

portfolio = read_portfolio(portfolio_path)
prices = read_prices(prices_path)

total_value = 0
for holding in portfolio:
    total_value += holding['price']*holding['shares']

current_value = 0
for holding in portfolio:
    current_value += prices[holding['name']]*holding['shares']

gain_loss = current_value - total_value

print('current portfolio value =', current_value)
print('gain/loss = ', gain_loss)

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
spacer = '-'*10
print(f'{spacer} {spacer} {spacer} {spacer}')
for name, shares, price, change in report:
    price = '$' + str(price)
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')