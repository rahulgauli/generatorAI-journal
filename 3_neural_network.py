import numpy as np 

inputs = [ 1, 2, 3 ,2.5 ]
weights = [
    [ 0.2, 0.8, -0.5, 1.0 ],
    [ 0.9, 0.5, -0.2, 3.0 ],
    [ 0.1, 0.11, -0.7, 2.0 ],
    [ 0.2, 0.14, 0.9, 4 ]
]
bias = [1, 2, 3, 1.2]


weights2 = [
    [0.1, -0.13, 0.5, 1.4],
    [-0.5, 0.12, -0.33, -0.1],
    [-0.44, 0.73, -0.13, -0.44],
    [0.2, 0.14, 0.9, 3]
]

biases2 = [-1, 2, -0.5, 1]

layer_1_output = np.dot(inputs, np.array(weights).T) + bias

layer_2_output = np.dot(layer_1_output, np.array(weights2).T + biases2)

print(layer_2_output)