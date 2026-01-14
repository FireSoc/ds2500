'''
3/18/25
DS 2500
Savir Khanna
Lecture
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.spatial.distance as ssd
TEST_FILE = "testing.csv"
TRAIN_FILE = "training.csv"
"""
1. read in the training, testing csv files into df, print
2. plot a scatterplot of training data (friendliness vs intelligence)
put the dogs and cats in different colors
3. pull out a row from training and a row from testing
compute the euclidean distance between them
4. make a list of distances from the testing row to ALL training rows
"""

def dataframe():
    train_df = pd.read_csv(TRAIN_FILE)
    test_df = pd.read_csv(TEST_FILE)
    return train_df, test_df

def scatterplot(train_df):
    train_df.plot(kind = "scatter", x = "friendliness", y = "intelligence")

def row_pull(train_df, test_df):
    r = np.random.randint(len(train_df))
    train_row = train_df[["friendliness", "intelligence"]].iloc[r]
    r = np.random.randint(len(test_df))
    test_row = test_df[["friendliness", "intelligence"]].iloc[r]
    return train_row, test_row

def euclidean(train_row, test_row):
    return ssd.euclidean(test_row, train_row)

def distance(train_df, train_row, test_row):
    dist = []
    for i in range(len(train_df)):
        train_row = train_df[["friendliness", "intelligence"]].iloc[i]
        d = ssd.euclidean(train_row, test_row)
        tup = (d, train_df.loc[i, "name"], train_df.loc[i, "label"])
        dist.append(tup)
    return dist

def get_k(dist):
    K = 3
    dist.sort()
    return dist[:K]

def find_majority_label(tups, labels, pos = 2):
    counts = {c : 0 for c in labels}
    for tup in tups:
        if tup[pos] in counts.keys():
            counts[tup[pos]] += 1
    return max(counts, key = counts.get)

def main():
    train_df, test_df = dataframe()
    train_df["color"] = np.where(train_df["label"] == "cat", "orange", "slateblue")

    scatterplot(train_df)
    train_row, test_row = row_pull(train_df, test_df)

    euclid = euclidean(train_row, test_row)

    dist = distance(train_df, train_row, test_row)
    closest_dist = get_k(dist)
    label = find_majority_label(closest_dist, ["dog", "cat"])
    print(label)
main()

