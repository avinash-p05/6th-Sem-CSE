import numpy as np

class Perceptron:

    def __init__(self,num_features,learning_rate=0.2,epochs=3):
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.array([-0.2, 0.4, 0])

    def activation_fn(self,x):
        return 1 if x>=0 else 0

    def predict(self,inputs):
        summation = np.dot(self.weights[1:],inputs) + self.weights[0]
        return self.activation_fn(summation)

    def fit(self,X,y):
        mse_history = []
        print(f"Initial Weights are {self.weights}")

        for epoch in range(self.epochs):
            total_error = 0
            predictions = []

            for inputs,label in zip(X,y):
                prediction = self.predict(inputs)
                error = label - prediction
                predictions.append([inputs,prediction])
                total_error +=error**2

                self.weights[1:] += self.learning_rate*inputs*error
                self.weights[0] += self.learning_rate*error

            mse = total_error/len(y)
            mse_history = mse
            print(f"Epoch {epoch+1}")
            print(f"Weights {self.weights}")
            print(f"Predictions : ")
            for input, prediction in predictions:
                print(f"Input : {input}   Prediction: {prediction}\n")
            print(f"Mean Squared Error : {mse:.4f}\n")

        return mse_history

X = np.array([
    [0, 0],[0, 1],[1, 0],[1, 1]]
)

y = np.array([0, 1, 1, 1])

preceptron = Perceptron(num_features=2)

mse_history = preceptron.fit(X,y)

print("The final Predictions : ")
for input in X:
    print(f"Inputs : {input}   Predictions : {preceptron.predict(input)}")

print(f"The final Weights are : {preceptron.weights}")