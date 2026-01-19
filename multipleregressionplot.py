import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [2104, 5, 1, 45],
    [1416, 3, 2, 40],
    [1534, 3, 2, 30],
    [852,  2, 1, 36]
], float)

y = np.array([460, 232, 315, 178], float)

# Add intercept
Xb = np.column_stack([np.ones(len(X)), X])

# Use pseudo-inverse (fixes singular matrix)
beta = np.linalg.pinv(Xb) @ y
print("Correct Coefficients:", beta)

# Predictions
y_pred = Xb @ beta

# Plot
plt.figure(figsize=(8,6))
plt.scatter(y, y_pred)
plt.plot([min(y), max(y)], [min(y), max(y)])
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Predicted vs Actual Price")
plt.show()
