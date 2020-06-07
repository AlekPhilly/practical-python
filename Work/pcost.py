# pcost.py
#
# Exercise 1.
import csv
import sys

def portfolio_cost(filename):
    with open(filename) as file:
        rows = csv.reader(file)
        cost = 0
        next(rows)
        for row in rows:
            try:
                qty = int(row[1])
                price = float(row[2])
                cost += qty*price
            except ValueError:
                print("Can't read the line")
                pass
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data\\portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)