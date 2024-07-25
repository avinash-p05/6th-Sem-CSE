import numpy as np

inputs = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
])

expectd_output = np.array(
    [1, -1, -1, -1]
)


weights = np.array([0.0 , 0.0])

bias = 0.0

print(f"Initial Weight : {weights} and Initial Bias is {bias}")

learning_rate = 1


def predict(input, weights, bias):
    weighted_sum = np.dot(input, weights)+bias
    return np.where(weighted_sum >= 0.0, 1, -1)

def print_truth_table(inputs, weights, bias):
    print("The Truth Table : ")
    for input in inputs:
        output = predict(input,weights,bias)
        print(f" {input}   |  {output}")





def hebbian_learning(inputs, expectd_output, weights, bias, learning_rate,epochs=4):
        for epoch in range(epochs):
            print(f" Epoch {epoch+1}")
            for i,x in enumerate(inputs):
                y=expectd_output[i]

                delta_weight = x * y * learning_rate
                delta_bias = y * learning_rate

                weights += delta_weight
                bias +=delta_bias

            print(f" The weights for Epoch {epoch+1} is {weights} ")
            print(f" The bias for Epoch {epoch + 1} is {bias} ")

            print_truth_table(inputs,weights,bias)

        return weights, bias



final_weights, final_bias = hebbian_learning(inputs, expectd_output, weights,bias, learning_rate)

print(f"\n final weights : {final_weights} and final bias : {final_bias}")