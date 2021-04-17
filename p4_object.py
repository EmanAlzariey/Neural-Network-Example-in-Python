import numpy as np

np.random.seed(0)

X =[[1, 2, 3, 2.5],   #need to normalize and scale this dataset to this range[-1,1]
    [2.0, 5.0, -1.0,2.0],
    [-1.5, 2.7, 3.3, -0.8]]

bais =[]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):  #n_inputs = how many features in a sample
        self.weights = 0.10*np.random.randn(n_inputs, n_neurons) #weight matrix
        self.biases = np.zeros((1, n_neurons)) #initially set bias to zero unless in special cases where output is zero put small value
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


# create instance of object
Layer1 = Layer_Dense(4,5)
Layer2 = Layer_Dense(5,2) #input must be output of Layer1

#output
Layer1.forward(X)
Layer2.forward(Layer1.output)


# print(Layer1.output)
print(Layer2.output)



# print( 0.10*np.random.randn(4, 3)) # randn method = same like guisian ..gives numbers around 1
#                                     # 4, 3 determines the shape of the weight batch (Matrix)
#                                     # multiply by 0.10 (normalized or scale) to smaller values