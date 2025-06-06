import math

p= [.7,.1,.2] 
target=[1,0,0]

loss=-(target[0]*math.log(p[0])+ target[1]*math.log(p[1])+
       target[2]*math.log(p[2]))

print(loss)

