import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load data
data = pd.read_csv("data.csv")

X = data[["age", "bp", "sugar", "bmi"]]
y = data["risk"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved")
