def euclidean(lst1, lst2):
    total = 0.0
    for i in range(len(lst1)):
        value = (lst1[i] - lst2[i]) ** 2
        total += value
    dist = pow(total, 0.5)
    return dist

def manhattan(lst1, lst2):
    dist = 0.0
    for i in range(len(lst1)):
        value = abs(lst1[i] - lst2[i])
        dist += value
    return dist

def hamming(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count +=1
    return count

'''
def jaccard(a, b):
    intersect = 0
    union = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            intersect += 1
'''