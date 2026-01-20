import numpy as np
import matplotlib.pyplot as plt


X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([5, 6, 10, 13, 11], dtype=float)


b0 = 3.3
b1 = 1.19
lr = 0.1


def batch_gradient_descent(X, Y, b0, b1, lr, iterations=10):
    n = len(X)
    history = []

    for i in range(iterations):
        y_pred = b0 + b1 * X

       
        db0 = (-2/n) * np.sum(Y - y_pred)
        db1 = (-2/n) * np.sum((Y - y_pred) * X)

        
        b0 = b0 - lr * db0
        b1 = b1 - lr * db1

      
        history.append((b0, b1, y_pred))

    return b0, b1, history


# -------- Stochastic Gradient Descent --------
def stochastic_gradient_descent(X, Y, b0, b1, lr, iterations=10):
    n = len(X)
    history = []

    for i in range(iterations):
        for j in range(n):   # take one sample at a time
            xj = X[j]
            yj = Y[j]
            y_pred = b0 + b1 * xj

            # Gradients
            db0 = -2 * (yj - y_pred)
            db1 = -2 * (yj - y_pred) * xj

            # Update parameters
            b0 -= lr * db0
            b1 -= lr * db1

        # Store each epoch
        y_pred_full = b0 + b1 * X
        history.append((b0, b1, y_pred_full))

    return b0, b1, history


# ---- Run BGD ----
b0_bgd, b1_bgd, bgd_hist = batch_gradient_descent(X, Y, b0, b1, lr)

# ---- Run SGD ----
b0_sgd, b1_sgd, sgd_hist = stochastic_gradient_descent(X, Y, b0, b1, lr)

# ---- Plotting ----
plt.figure(figsize=(14, 6))

# Batch GD plot
for i, (_, _, y_pred) in enumerate(bgd_hist):
    plt.plot(X, y_pred, label=f'BGD Iter {i+1}')

plt.scatter(X, Y, color='black')
plt.title("Batch Gradient Descent (10 Iterations)")
plt.legend()
plt.show()

# SGD plot
plt.figure(figsize=(14, 6))

for i, (_, _, y_pred) in enumerate(sgd_hist):
    plt.plot(X, y_pred, label=f'SGD Iter {i+1}')

plt.scatter(X, Y, color='black')
plt.title("Stochastic Gradient Descent (10 Iterations)")
plt.legend()
plt.show()
