'''
accuracy - % of predictions that are correct
precision - % of things predicted label + are actually label A
recall - % of actual label A's first 1 predicted as label A
F1 - (prec * recall) * 2/(prec+recall)
MSE - (prec-actual)^2 is the average of all error, lower is better
Multiple logistic regression:
    sigmoid function
    0<x<1
    probabilistic: >0.5 yes label, <0.5 no/not applied
'''
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
y = np.array([0, 0, 0, 1, 1, 1])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)

# Predict probabilities
probabilities = model.predict_proba(X_test)
print("Predicted Probabilities:\n", probabilities)