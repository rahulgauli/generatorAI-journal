import numpy as np

input = [ 
    0.5,
    0.8,
    1,
    1.3
]

weights = [ 
    1,
    2,
    0.5,
    -1
 ]

bias = 2

value = np.dot(input, weights) + bias
print(value)