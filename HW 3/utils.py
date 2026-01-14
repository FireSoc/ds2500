import csv

def read_csv(filename):
    ''' given the name of a csv file, return its contents as a 2d list,
        including the header.'''
    data = {}
    with open(filename,"r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        for row in csvfile:
            key = row[0]
            values = [float(val) for val in row[1:]]
            data[key] = values
    return data

def name_conversion(data):
    """
    Parameter: data: A 2D list of a dataset
    Does: Converting all strings in the first column of data to
    lowercase and no whitespace
    Returns: A new 2D list of data
    """
    converted_data = []
    for row in data:
        # Converting row[0] to a separate list to concatenate with the list of the list in row
        name = row[0].replace(" ", "").lower()
        converted_data.append([name] + row[1:])
    return converted_data