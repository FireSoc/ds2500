import csv

def read_csv(filename, skip = 1):
    ''' given the name of a csv file, return its contents as a 2d list,
        including the header.'''
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for _ in range(skip):
            next(csvfile)
        for row in csvfile:
            data.append(row)
    return data

def lst_to_dct(lst):
    ''' given a 2d list, create and return a dictionary.
        keys of the dictionary come from the header (first
                                                     row)
        , values are corresponding columns, saved as lists
        Ex: [[1, 2, 3], [x, y, z], [a, b, c]]
        should return {1 : [x, a], 2 : [y, b], 3 : [z, c]}
    '''
    dct = {h : [] for h in lst[0]}
    for row in lst[1:]:
        for i in range(len(row)):
            dct[lst[0][i]].append(row[i])
    return dct


def main():
    print("Hello I am the utility function file!")


if __name__ == "__main__":
    main()