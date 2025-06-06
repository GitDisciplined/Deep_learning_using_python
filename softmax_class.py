
import numpy as np

class softmax_activation():

    def softmax(self,inputs):

        self.x=np.exp(inputs)/sum(np.exp(inputs))

        return self.x


activation=softmax_activation()

output=activation.softmax([4.8,1.21,2.385])



        
