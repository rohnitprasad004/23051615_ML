import numpy as np
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([5, 6, 10, 13, 11], dtype=float)
b0 = 3.3
b1 = 1.19
lr = 0.1
def batch_gradient_descent(X, Y, b0, b1, lr, iterations=10):
    n = len(X)

    print("---- Batch Gradient Descent ----") 
    for i in range(iterations):
        y_pred = b0 + b1 * X
        db0 = (-2/n) * np.sum(Y - y_pred)
        db1 = (-2/n) * np.sum((Y - y_pred) * X)
        b0 = b0 - lr * db0
        b1 = b1 - lr * db1

        print(f"Iter {i+1}: b0 = {b0:.4f}, b1 = {b1:.4f}")

    return b0, b1
def stochastic_gradient_descent(X, Y, b0, b1, lr, iterations=10):
    n = len(X)

    print("\n---- Stochastic Gradient Descent ----")
    for i in range(iterations):
        for j in range(n):  
            xj = X[j]
            yj = Y[j]
            y_pred = b0 + b1 * xj
            db0 = -2 * (yj - y_pred)
            db1 = -2 * (yj - y_pred) * xj
            b0 -= lr * db0
            b1 -= lr * db1

        print(f"Iter {i+1}: b0 = {b0:.4f}, b1 = {b1:.4f}")

    return b0, b1

batch_gradient_descent(X, Y, 3.3, 1.19, lr=0.1)
stochastic_gradient_descent(X, Y, 3.3, 1.19, lr=0.1)
