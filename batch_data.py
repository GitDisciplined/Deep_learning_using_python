
#batch data to a layer of 3 neurons

import numpy as np


inputs=np.array([[1,2,3,2.5],[2,5,-1,2],[-1.5,2.7,3.3,-.8]])

weights=np.array([[.2,.8,-.5,1],[.5,-.91,.26,-.5],[-.26,-.27,.17,.87]])


bias=np.array([2,3,.5])

output= np.dot(inputs,weights.T)+bias


