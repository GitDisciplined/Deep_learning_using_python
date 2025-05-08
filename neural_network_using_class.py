import numpy as  np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

class dense_layer():

    #weight matrix and bias vector initilization

    def __init__(self,n_inputs,n_neurons):

        self.weights=.01*np.random.randn(n_inputs,n_neurons)
        self.biases=np.zeros((1,n_neurons))


    # output of a layer
    def  forward(self,inputs):


        self.output=np.dot(inputs,self.weights)+ self.biases
        return self.output

#creating data set

x,y= spiral_data(samples=100,classes=3)




layer1= dense_layer(2,4)

out_layer1=layer1.forward(x)



