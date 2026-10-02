import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Gradient descent loop
    for _ in range(iterations):
        # 1. Compute predictions: h_θ(X) = X @ θ, shape (m, 1)
        predictions = X @ theta
        
        # 2. Compute error: (h_θ(X) - y), shape (m, 1)
        error = predictions - y
        
        # 3. Compute gradient of MSE loss:
        #    ∇L(θ) = (1/m) * Xᵀ @ (h_θ(X) - y), shape (n, 1)
        gradient = (1 / m) * (X.T @ error)
        
        # 4. Update weights: θ := θ - α * ∇L(θ)
        theta = theta - alpha * gradient

    return theta.flatten()