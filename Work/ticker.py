from follow import follow
import csv
import report
import tableformat

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    # rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
        yield (dict(zip(headers, row)) for row in rows)

def filter_symbols(rows, names):
     yield (row for row in rows if row['name'] in names)

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])
    for row in rows:
        formatter.row(row)



if __name__ == "__main__":
    lines = follow('Data\\stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)