import numpy as np
from numpy.typing import NDArray
from typing import Any

class Linear_Regression_Model:
    def __init__(self, features: NDArray[Any], response: NDArray[Any]) -> None:
        self.features = features
        self.response = response
        self.weights = np.random.rand(self.features.shape[1])
        self.bias = np.random.rand(1).item()  # Initialize as a scalar
    
    def compute_prediction(self) -> NDArray[np.float64]:
        return np.dot(self.features, self.weights) + self.bias

    def compute_cost(self) -> float:
        m = len(self.response)
        yhat = self.compute_prediction()
        errors = yhat - self.response
        j = (1 / (2 * m)) * np.sum(np.square(errors))  # Mean squared error
        return j

    def train(self, epochs=1000, alpha=0.01) -> None:
        m = len(self.response)
        
        for epoch in range(epochs):
            yhat = self.compute_prediction()
            errors = yhat - self.response
            
            # Compute gradients
            weight_gradients = (1 / m) * np.dot(self.features.T, errors)
            bias_gradient = (1 / m) * np.sum(errors)
            
            # Update weights and bias
            self.weights -= alpha * weight_gradients
            self.bias -= alpha * bias_gradient
            
            # Optionally print the cost every 100 epochs
            if epoch % 100 == 0:
                cost = self.compute_cost()
                print(f'Epoch {epoch}, Cost: {cost}')

# Example usage
features = np.array([[1, 2], [2, 3], [3, 4]])
response = np.array([3, 5, 7])
model = Linear_Regression_Model(features, response)
model.train(epochs=1000, alpha=0.01)
