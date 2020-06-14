# pcost.py
#
# Exercise 1.
import csv
import sys
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(cl_options):
    cost = portfolio_cost(cl_options[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data\\portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)