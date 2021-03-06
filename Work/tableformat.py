class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        rowdata = [ str(record) for record in rowdata ]
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        rowdata = [ str(record) for record in rowdata ]
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        rowdata = [ str(record) for record in rowdata ]
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt=='txt':
        formatter = TextTableFormatter()
    elif fmt=='csv':
        formatter = CSVTableFormatter()
    elif fmt=='html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'unknown table format {fmt}')
    return formatter

def print_table(lines, select, formatter):
    formatter.headings(select)
    for line in lines:
        rowdata = [ str(getattr(line, attr)) for attr in select ]
        formatter.row(rowdata)        
        
