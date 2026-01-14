'''
Savir Khanna
DS 2500
HW 3
Spring 2025
'''

import math

def euclidean(lst1, lst2):
    """
    Computes the Euclidean distance between two lists of numerical values.
    :param lst1: First list of numerical values.
    :param lst2: Second list of numerical values.
    :return: Euclidean distance rounded to three decimal places.
    """
    total = 0.0
    for i in range(len(lst1)):
        value = (lst1[i] - lst2[i]) ** 2
        total += value
    dist = math.sqrt(total)
    return round(dist, 3)

def manhattan(lst1, lst2):
    """
    Computes the Manhattan distance between two lists of numerical values.
    :param lst1: First list of numerical values.
    :param lst2: Second list of numerical values.
    :return: Manhattan distance.
    """
    dist = 0
    for i in range(len(lst1)):
        value = abs(lst1[i] - lst2[i])
        dist += value
    return dist

def hamming(a, b):
    """
    Computes the Hamming distance between two strings or lists.
    :param a: First string or list.
    :param b: Second string or list.
    :return: Hamming distance.
    """
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

def jaccard(lst1, lst2):
    """
    Computes the Jaccard similarity coefficient between two binary lists.
    :param lst1: First binary list.
    :param lst2: Second binary list.
    :return: Jaccard similarity coefficient.
    """
    intersection = 0
    union = 0
    for i in range(len(lst1)):
        if lst1[i] == 1 and lst2[i] == 1:
            intersection += 1
        if lst1[i] == 1 or lst2[i] == 1:
            union += 1
    return intersection / union

def test_euclidean():
    assert euclidean([],[]) == 0
    assert euclidean([0],[0]) == 0
    assert euclidean([2,4], [4,2]) == 2.828
    assert euclidean([1,2,3], [4,5,6]) == 5.196
    assert euclidean([9,4,6], [3,4,8]) == 6.325

def test_manhattan():
    assert manhattan([], []) == 0
    assert manhattan([0], [0]) == 0
    assert manhattan([3,4], [8,10]) == 11

def test_hamming():
    assert hamming("", "") == 0
    assert hamming("popping", "running") == 4
    assert hamming("indifference", "undecidedese") == 9
    assert hamming([1,2,4,5], [36, 8, 4, 5]) == 2

def test_jaccard():
    assert jaccard([1,1,1,0], [0,0,1,1]) == 0.25
    assert jaccard([1,0,1], [1,0,0]) == 0.5
    assert jaccard([1,1], [1,1]) == 1

def main():
    """
    Runs test functions for distance and similarity metrics.
    """
    test_euclidean()
    test_manhattan()
    test_hamming()
    test_jaccard()
    print("All tests passed successfully.")

if __name__ == '__main__':
    main()
