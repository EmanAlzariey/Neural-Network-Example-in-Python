inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]


layer_outputs = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 #output of given neuron
    for n_inputs, weight in zip (inputs, neuron_weights):
        neuron_output += n_inputs*weight

    neuron_output += neuron_bias # add the bias of each neuron at the end
    layer_outputs.append(neuron_output) #append each output to the array or list


print(layer_outputs)




#  note: zip is an iterator of tuples where the first item in each passed iterator is paired together,
#   and then the second item in each passed iterator are paired together etc
# Thus output is a tuple (weight[0] with bias[0])