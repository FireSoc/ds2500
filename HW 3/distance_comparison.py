'''
Savir Khanna
DS 2500
HW 3
Spring 2025
'''
from utils import *
from test_distances import *
import matplotlib.pyplot as plt

FILENAME1 = "data/hw3_dataset_numeric.csv"
FILENAME2 = "data/hw3_dataset_binary.csv"

def euclidean_dist(data, row1, row2):
    """
    Computes the Euclidean distance between two rows in the dataset.
    :param data: Dict containing dataset rows as keys and feature lists as values.
    :param row1: row used in calculations
    :param row2: 2nd row used in calculations
    :return: Euclidean distance between row1 and row2.
    """
    for key in data:
        for key2 in data:
            if key == row1 and key2 == row2:
                dist = euclidean(data[key], data[key2])
                break
    return dist

def manhattan_dist(data, row1, row2):
    """
    Finds the Manhattan distance between two rows in the dataset.
    :param data: Dict containing dataset rows as keys and feature lists as values.
    :param row1: row used in calculations
    :param row2: 2nd row used in calculations
    :return: Manhattan dist between row1 and row2.
    """
    for key in data:
        for key2 in data:
            if key == row1 and key2 == row2:
                dist = manhattan(data[key], data[key2])
                break
    return dist

def jaccard_dist_values(data):
    """
    Calculates the average Jaccard distance and a list of all Jaccard distances in the dataset.
    :param data: Dictionary containing dataset rows as keys and feature lists as values.
    :return: avg distance calculated and list of all distances
    """
    dist = 0
    count = 0
    jaccard_dist = []
    for key in data:
        for key2 in data:
            if key2 != key:
                distance = jaccard(data[key], data[key2])
                dist += distance
                jaccard_dist.append(distance)
                count += 1
    avg_dist = dist / count
    return avg_dist, jaccard_dist

def hamming_dist_values(data):
    """
    Computes the average Hamming distance and a list of all Hamming distances in the dataset.
    :param data: Dict containing dataset rows as keys and feature lists as values.
    :return: avg distance calculated and list of all distances
    """
    dist = 0
    count = 0
    hamming_dist = []
    for key in data:
        for key2 in data:
            if key != key2:
                distance = hamming(data[key], data[key2])
                dist += distance
                hamming_dist.append(distance)
                count += 1
    avg_dist = dist / count
    return avg_dist, hamming_dist

def avg_dist(distance_type, data, row):
    """
    Finds the average distance for all rows for euclidean or manhattan.
    :param distance_type: String with type of distance ('euclidean' or 'manhattan').
    :param data: Dict that has dataset rows as keys and feature lists as values.
    :param row: row for distance
    :return: avg distance calculated and list of all distances
    """
    total_dist = 0
    euclidean = []
    manhattan = []
    for key in data:
        if distance_type == 'euclidean':
            distance = euclidean_dist(data, row, key)
            total_dist += distance
            euclidean.append(distance)
        elif distance_type == 'manhattan':
            distance = manhattan_dist(data, row, key)
            total_dist += distance
            manhattan.append(distance)
    avg_dist = total_dist / (len(data) - 1)

    euclidean = euclidean[1:]
    manhattan = manhattan[1:]

    if euclidean:
        return avg_dist, euclidean
    elif manhattan:
        return avg_dist, manhattan

def plot_vals_eu_mh(lst1, lst2, name1, name2):
    """
    Plots a scatter plot comparing Euclidean and Manhattan distances.
    :param lst1: List of Euclidean distances.
    :param lst2: List of Manhattan distances.
    :param name1: name of the lst1
    :param name2: name of lst2
    """
    plt.scatter(lst1, lst2)
    plt.xlabel(f"{name1} Distances")
    plt.ylabel(f"{name2} Distances")
    plt.title(f"{name1} Distances vs {name2} Distances")
    plt.xlim(0, 20)
    plt.ylim(0, 40)
    plt.show()

def plot_vals_jc_hm(lst1, lst2, name1, name2):
    """
    Plots a scatter plot comparing Jaccard and Hamming distances.
    :param lst1: List of Jaccard distances.
    :param lst2: List of Hamming distances.
    :param name1: name of lst1
    :param name2: name of lst2
    """
    plt.scatter(lst1, lst2)
    plt.xlabel(f"{name1} Distances")
    plt.ylabel(f"{name2} Distances")
    plt.title(f"{name1} Distances vs {name2} Distances")
    plt.show()

def main():
    """
    Main function to read data, compute distances, and plot results.
    """
    data1 = read_csv(FILENAME1)
    data2 = read_csv(FILENAME2)

    alpha_eu_mean_dist, euclidean_dist_lst = avg_dist("euclidean", data1, "Alpha")
    print("The average Euclidean distance from Alpha row is ",
          round(alpha_eu_mean_dist,3), ".", sep="")

    alpha_mh_mean_dist, manhattan_dist_lst = avg_dist("manhattan", data1, "Alpha")
    print("The average Manhattan distance from Alpha row is ",
          round(alpha_mh_mean_dist, 3), ".", sep="")

    mean_jc_index, jaccard_dist_lst = jaccard_dist_values(data2)
    print("The average Jaccard distance is ", round(mean_jc_index,3), ".", sep="")

    mean_hm_index, hamming_dist_lst = hamming_dist_values(data2)
    print("The average Hamming distance is ", round(mean_hm_index, 3), ".", sep="")

    plot_vals_eu_mh(euclidean_dist_lst, manhattan_dist_lst, "Euclidean", "Manhattan")
    plot_vals_jc_hm(jaccard_dist_lst, hamming_dist_lst, "Jaccard", "Hamming")

if __name__ == '__main__':
    main()
