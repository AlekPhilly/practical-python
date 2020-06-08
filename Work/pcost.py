# pcost.py
#
# Exercise 1.
import csv
import sys

def portfolio_cost(filename):
    with open(filename) as file:
        rows = csv.reader(file)
        cost = 0
        headers = next(rows)
        for num, row in enumerate(rows, start=1):
            record = dict(zip(headers,row))
            try:
                qty = int(record['shares'])
                price = float(record['price'])
                cost += qty*price
            except ValueError:
                print(f"Row {num}: Couldn't convert: {row}")
                continue
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data\\portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)