def generate_lst_short(max_square):
    lst = [x**2 for x in range(1, max_square) if x % 2 == 0]
    return lst

def spam(lst1, lst2):
    count = 0
    set = {1}
    newlst = [val2 for val in lst1 for val2 in lst2 if val == val2]
    for x in newlst:
        set.add(x)
    for x in range(len(set)):
        count += 1
    set.remove(1)
    return newlst

def max_by_length(dct1):
    
