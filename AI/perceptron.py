
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.random.rand(input_size)
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.bias = np.random.rand(1)
    
    def activate(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        return self.activate(summation)
    
    def train(self, training_data, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                self.weights += self.learning_rate * (label - prediction) * inputs
                self.bias += self.learning_rate * (label - prediction)

def main():
    # AND gate training data
    training_data = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    labels = np.array([0, 0, 0, 1])
    
    # Create a perceptron with 2 input neurons (matching the AND gate input size)
    perceptron = Perceptron(input_size=2)
    
    # Train the perceptron
    perceptron.train(training_data, labels)
    
    # Test the perceptron
    test_data = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    
    print("Test Results:")
    for inputs in test_data:
        prediction = perceptron.predict(inputs)
        print(f"Inputs: {inputs}, Prediction: {prediction}")

if __name__ == "__main__":
    main()
