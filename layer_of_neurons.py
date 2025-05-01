
import numpy as np



inputs=[1,2,3,2.5]

weights1=[.2,.8,-.5,1]

weights2=[.5,-.91,.26,-.5]

weights3=[-.26,-.27,.17,.87]

bias1=2
bias2=3
bias3=.5


out1=np.dot(inputs,weights1)+bias1
out2=np.dot(inputs,weights2)+bias2
out3=np.dot(inputs,weights3)+bias3

out= [out1, out2,out3]
