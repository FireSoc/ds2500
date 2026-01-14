import pandas as pd
import numpy as np
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

wine_data = sklearn.datasets.load_wine(as_frame=True)
df_wine = wine_data.frame

X = df_wine.drop(columns=["target"])
Y = df_wine["target"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
print(df_wine.columns)

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, Y_train)
pred = knn.predict(X_test)

comparison_df = pd.DataFrame({"Actual": Y_test.values, "Predicted": pred})

k = 0
for i in range(len(comparison_df)):
    if comparison_df.loc[i, "Actual"] != comparison_df.loc[i, "Predicted"]:
        k += 1

print(k)

print(comparison_df)
