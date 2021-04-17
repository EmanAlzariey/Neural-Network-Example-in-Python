import numpy as np

# multiple inputs (generlize the neuron learning .. in practical apps chhose batch 32(more common) or 64 )
inputs =[[1, 2, 3, 2.5],
        [2.0, 5.0, -1.0,2.0],
        [-1.5, 2.7, 3.3, -0.8]]


weights_matrix = [[0.2, 0.8, -0.5, 1],       #batch is parallel number of lists in a list (matrix)
                  [0.5, -0.91, 0.26, -0.5],
                  [-0.26, -0.27, 0.17, 0.87]] 

biases = [2, 3, 0.5]

weights_matrix2 = [[0.1, -0.14, 0.5],       #batch is parallel number of lists in a list (matrix)
                  [-0.5, 0.12, 0.33],
                  [-0.44, 0.73, -0.13]] 

biases2 = [-1, 2, -0.5]

output_layer1 = np.dot(  inputs, np.array(weights_matrix).T) + biases  #np.transpose(weights_matrix) = np.array(weights_matrix).T

output_layer2 = np.dot(  output_layer1, np.array(weights_matrix2).T) + biases2

print(output_layer2)