# importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# defining constants
FILENAME = "demographics.csv"
FILENAME2 = "1976-2020-president.tab"

def read_tab_file(filename, header=""):
    """
    Reads a tab-delimited file into a pandas DataFrame.
    :param filename: The name of the file to read.
    :param header: Optional header for raw data (not used).
    :return: A pandas df containing the file data.
    """
    df = pd.read_csv(filename, delimiter='\t')
    return df

def create_classifier(df, k):
    """
    Creates and trains a k-Nearest Neighbors classifier.
    :param df: merged df that contains features and labels.
    :param k: The number of neighbors for the KNN classifier.
    :return: Predicted labels, training and testing datasets.
    """
    X = df[["male_pct", "female_pct", "white_alone_pct", "black_pct", "hispanic_pct"]]
    Y = df["party_detailed"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, Y_train)
    pred = knn.predict(X_test)

    return pred, X_train, X_test, Y_train, Y_test

def clean_data(year):
    """
    Cleans and merges demographic and election data for a given year.
    :param year: The election year to filter data for.
    :return: Merged df for demo and pres
    """
    df_demo = pd.read_csv(FILENAME)
    df_pres = read_tab_file(FILENAME2)

    df_demo = df_demo.rename(columns={'STNAME': 'state', 'FIPS': "state_fips"})
    df_pres = df_pres[df_pres["year"] == year]

    df_demo["state"] = df_demo["state"].str.strip().str.lower()
    df_pres["state"] = df_pres["state"].str.strip().str.lower()

    df_pres = df_pres.loc[df_pres.groupby("state")["candidatevotes"].idxmax()]
    df_pres = df_pres[["state", "party_detailed"]].reset_index(drop=True)

    merged_df = pd.merge(df_demo, df_pres, on="state", how="left")
    return merged_df, df_demo, df_pres

def features_calc(df):
    """
    Calculates demographic feature percentages and selects relevant columns.
    :param df: the merged df of demo and pres
    :return: A filtered df with calculated feature percentages.
    """
    df["male_pct"] = df["TOT_MALE"] / df["TOT_POP"]
    df["female_pct"] = df["TOT_FEMALE"] / df["TOT_POP"]
    df["white_alone_pct"] = (df["WA_MALE"] + df["WA_FEMALE"]) / df["TOT_POP"]
    df["black_pct"] = df["Black"] / df["TOT_POP"]
    df["hispanic_pct"] = df["Hispanic"] / df["TOT_POP"]

    df = df[["state", "male_pct", "female_pct",
            "white_alone_pct", "black_pct", "hispanic_pct", "party_detailed"]]
    return df

def accuracy(df, min_k, max_k):
    """
    Computes the accuracy of KNN models for different k values.
    :param df: The DataFrame containing feature data.
    :param min_k: The minimum k value to test.
    :param max_k: The maximum k value to test.
    :return: The most accurate k value and the number of correctly predicted states.
    """
    accuracies = []
    for i in range(min_k, max_k):
        pred, x_train, x_test, y_train, y_test = create_classifier(df, i)
        accuracy = accuracy_score(y_test, pred)
        accuracies.append(accuracy)
    highest_acc = accuracies.index(max(accuracies))
    highest_acc += min_k

    states_predicted = round(max(accuracies) * len(y_test))
    return highest_acc, states_predicted

def plot_heatmap(y_test, pred, k):
    """
    Plots a confusion matrix heatmap for the classifier results.
    :param y_test: The actual labels.
    :param pred: The predicted labels.
    :param k: The k-value used in the classifier.
    """
    cm = confusion_matrix(y_test, pred)
    sns.heatmap(cm, annot=True, xticklabels=["Republican", "Democrat"], yticklabels=["Republican", "Democrat"])
    plt.title(f"Confusion Matrix: k={k}")
    plt.ylabel("Actual Values")
    plt.xlabel("Predicted Values")
    plt.show()

def plot_scatter(df):
    """
    Plots a scatter plot comparing White and Hispanic population percentages.
    :param df: The DataFrame containing demographic data.
    """
    sns.scatterplot(x=df["white_alone_pct"], y=df["hispanic_pct"],
                    hue=df["party_detailed"], style=df["party_detailed"])
    plt.title("White vs Hispanic % of Total Population")
    plt.xlabel("White Alone (%)")
    plt.ylabel("Hispanic (%)")
    plt.legend()
    plt.show()

def main():
    """
    Main function to execute the election prediction analysis.
    """
    year = int(input("What election year would you like between 1976 and 2020? "))
    merged_df, df_demo, df_pres = clean_data(year)
    merged_df = features_calc(merged_df)

    pred, x_train, x_test, y_train, y_test = create_classifier(merged_df, 3)
    comparison_df = pd.DataFrame({"Actual": y_test.values, "Predicted": pred})
    f1 = f1_score(comparison_df['Actual'], comparison_df['Predicted'], pos_label="DEMOCRAT")
    best_k_3, states_predicted_3 = accuracy(merged_df, 3, 4)

    print(states_predicted_3, "states were predicted correctly when k=3.")
    print("The length of the training set is:", len(y_train))
    print("The f1 score for democrat when k=3 is", round(f1, 2))

    best_k_5_11, states_predicted_5_11 = accuracy(merged_df, 5, 11)

    print(f"The k-value with the highest accuracy is {best_k_5_11}.")
    print(f"The highest states predicted for k-values 5-11 is {states_predicted_5_11}.")

    plot_heatmap(y_test, pred, best_k_5_11)
    plot_scatter(merged_df)

if __name__ == "__main__":
    main()
