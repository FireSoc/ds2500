'''
DS2500
Spring 2025

utils.py - functions that we use over and over again
'''
import csv
def read_csv(filename, skip = 1):
    '''
    param: filename string and skip (optional) for # of lines to skip
    :param skip:
    does: reads in the CSV file using CSV library
    '''
    data = []
    with open(filename, 'r') as infile:
        csvfile = csv.reader(infile)
        for _ in range(skip):
            next(csvfile)
        for row in csvfile:
            data.append(row)
    return data

def col_to_lst(lst, col_no):
    "converting a column of dataset to 1D lst"
    newlst = []
    for row in lst:
        newlst.append(row[col_no])
    return newlst

def clean_currency(s):
    '''given a string in the form &xx,xxx
    compute and return float'''
    s = s.replace("$", "")
    s = s.replace(",", "")
    return float(s)