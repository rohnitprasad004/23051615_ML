import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


data = {
    "Income": [
        60, 75, 85.5, 52.8, 64.0, 64.8, 51.5, 43.2, 87, 84,
        110.1, 49.2, 108, 52.2, 92.8, 66, 69, 47.4, 93, 33,
        51, 51, 81, 63
    ],
    "LawnSize": [
        18.4, 19.6, 15.8, 70.8, 21.6, 17.2, 20.8, 20.4, 23.6, 17.6,
        19.2, 17.6, 17.6, 16, 22.4, 18.4, 20, 16.4, 20.0, 18.8,
        22, 14, 20, 14.0
    ],
    "Decision": [
        "Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner",
        "Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner",
        "Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner",
        "Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner"
    ]
}

df = pd.DataFrame(data)


le = LabelEncoder()
df["Decision"] = le.fit_transform(df["Decision"])


X = df[["Income", "LawnSize"]]
y = df["Decision"]

model = DecisionTreeClassifier(criterion="gini", max_depth=3)
model.fit(X, y)


plt.figure(figsize=(14, 8))
plot_tree(
    model,
    feature_names=["Income", "LawnSize"],
    class_names=["Nonowner", "Owner"],
    filled=True
)
plt.show()


sample = [[70, 20]]
prediction = model.predict(sample)
print("Prediction:", le.inverse_transform(prediction))
