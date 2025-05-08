import numpy as np



#input layer

inputs=np.array([[1,2,3,2.5],[2,5,-1,2],[-1.5,2.7,3.3,-.8]])


# weights of first hidden layer

weights1=np.array([[.2,.8,-.5,1],[.5,-.91,.26,-.5],[-.26,-.27,.17,.87]])


#bias of first hidden layer

bias1= np.array([2,3,.5])


#ouput of first hidden layer


output1=np.dot(inputs,weights1.T)+bias1


# weights of second hidden layer

weights2=np.array([[.1,-.14,.5],[-.5,.12,-.33],[-.44,.73,-.13]])


#bias of first hidden layer

bias2= np.array([-1,2,-.5])


#output of second hidden layer


output2=np.dot(output1,weights2.T)+bias2



print(output2)

