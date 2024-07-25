import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

inputs = np.array([
    [0,0],[0,1],[1,0],[1,1]
])

expected_output = np.array([[0],[1],[1],[0]])

epochs = 10000
lr=0.5
i_l_n , h_l_n, o_l_n = 2,2,1

hidden_weights = np.random.uniform(size=(i_l_n,h_l_n))
hidden_bias = np.random.uniform(size=(1,h_l_n))
output_weights = np.random.uniform(size=(h_l_n,o_l_n))
output_bias = np.random.uniform(size=(1,o_l_n))

print("Initial Hidden Weights: ",end=' ')
print(*hidden_weights)
print("Initial Hidden Bias: ",end=' ')
print(*hidden_bias)
print("Initial Output Weights: ",end=' ')
print(*output_weights)
print("Initial Output Bias: ",end=' ')
print(*output_bias)

for _ in range(epochs):
    h_l_a = np.dot(inputs,hidden_weights)
    h_l_a += hidden_bias
    h_l_opt = sigmoid(h_l_a)

    o_l_a = np.dot(h_l_opt,output_weights)
    o_l_a += output_bias
    predicted_output = sigmoid(o_l_a)

    error = expected_output - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    e_h_l = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = e_h_l * sigmoid_derivative(h_l_opt)

    output_weights += h_l_opt.T.dot(d_predicted_output)*lr
    output_bias += np.sum(d_predicted_output,axis=0,keepdims=True)*lr

    hidden_weights += inputs.T.dot(d_hidden_layer)*lr
    hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True)*lr

print("Final hidden weights : ",end=' ')
print(*hidden_weights)
print("Final hidden bias : ",end=' ')
print(*hidden_bias)
print("Final output weights : ",end=' ')
print(*output_weights)
print("Final output bias : ",end=' ')
print(*output_bias)

print("\n Output from neural network after epoch ",str(epochs))
print(*predicted_output)

