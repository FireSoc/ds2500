'''
Savir Khanna
HW 1
DS2500
Spring 2025
utils.py - functions that we use over and over again
'''
import csv
def read_csv(filename, skip = 1):
    '''
    param: filename string and skip (optional) for # of lines to skip
    does: reads in the CSV file using CSV library, and also replaces
    any blanks with zeros
    '''
    data = []
    with open(filename, 'r') as infile:
        csvfile = csv.reader(infile)
        for _ in range(skip):
            next(csvfile)
        for row in csvfile:
            data.append(row)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "":
                data[i][j] = 0
    return data

def find_team_names(data):
    """
    param: 2D list of goals data
    return: the individual teams in order
    """
    teams = []
    for i in range(len(data)):
        teams.append(data[i][0])
    return teams
