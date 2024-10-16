import numpy as np
class NeuralNetwork:
    def __init__(self):
        np.random.seed()
        self.weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, inputs, outputs, iterations):
        for _ in range(iterations):
            output = self.think(inputs)
            self.weights += np.dot(inputs.T, (outputs - output) * self.sigmoid_derivative(output))

    def think(self, inputs):
        return self.sigmoid(np.dot(inputs.astype(float), self.weights))

if __name__ == "__main__":
    nn = NeuralNetwork()
    print("Beginning Randomly Generated Weights:\n", nn.weights)

    inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    outputs = np.array([[0, 1, 1, 0]]).T

    nn.train(inputs, outputs, 15000)
    print("Ending Weights After Training:\n", nn.weights)

    user_input = np.array([int(input(f"Input {i+1}: ")) for i in range(3)])
    print("Considering New Situation:", *user_input)

    print("New Output data:\n", nn.think(user_input))
