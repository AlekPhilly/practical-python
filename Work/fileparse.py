# fileparse.py
#
# Exercise 3.3
import  csv 


def parse_csv(rows, select=None, types=None, has_headers=True, delimiter=',',
                silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if isinstance(rows, str):
        raise ValueError("input isn't iterable!")
    if (select) and (not has_headers): 
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(rows, delimiter=delimiter)
    # Read the file headers 
    headers = next(rows) if has_headers else []
       
    if select:
        indices = [headers.index(column) for column in select]
        headers = select

    records = []    
    for n, row in enumerate(rows, start=1):
        if not row: # Skip rows with no data
            continue
        
        if select:
            row = [row[index] for index in indices]      
        
        if types:
            try:          
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:    
                    print(f"Row {n}: Couldn't convert {row}")
                    print(f'Row {n}: Reason {e}')
                continue

        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records

    # with open(filename) as f:
    #     rows = csv.reader(f, delimiter=delimiter)