import numpy as np #in cmd >> pip install numpy ; conda activate base 
print("Numpy:", np.__version__)
inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1]
bias = 2

output = np.dot(inputs, weights) + bias # if one neuron can start with inputs or weights, both is correct
                                        # shape is (4,) output is single number

print(output)

inputs = [1, 2, 3, 2.5]

weights_matrix = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

output2 = np.dot(weights_matrix, inputs) + biases # if more than one neuron must start with weights 
                                        #shape of matrix weight is (3, 4) output would be vector (4,)

print(output2)