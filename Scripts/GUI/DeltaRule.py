import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ReglaDelta:
    def __init__(self, input_size, learning_rate):
        self.weights = np.random.rand(input_size + 1)  # +1 para el sesgo
        self.learning_rate = learning_rate
        self.errors = []

    def predict(self, X):
        X = np.insert(X, 0, 1)  # Insertar 1 para el sesgo
        activation = np.dot(self.weights, X)
        return self.step_function(activation)

    def step_function(self, activation):
        return 1 if activation >= 0 else 0

    def train(self, X_train, y_train, epochs):
        for epoch in range(epochs):
            error_epoch = 0
            for X, y in zip(X_train, y_train):
                prediction = self.predict(X)
                error = y - prediction
                X = np.insert(X, 0, 1)  # Insertar 1 para el sesgo
                self.weights += self.learning_rate * error * X
                error_epoch += error ** 2  # Error cuadrático
            self.errors.append(error_epoch)

    def plot_errors(self):
        plt.plot(self.errors)
        plt.xlabel('Iteracion')
        plt.ylabel('Error cuadrático')
        plt.title('Evolución del error durante el entrenamiento')
        plt.show()

    def count_errors(self, X_test, y_test):
        predictions = [self.predict(X) for X in X_test]
        errors = sum(y_test != predictions)
        return errors