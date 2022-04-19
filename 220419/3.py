import numpy as np
from numpy.linalg import inv
A=np.array(range(1,10)).reshape(3,3)
print(inv(A))

#2x-y=0
#x+y=3
#Y=WX
#W=YX^-1
X=np.array([[2,-1],[1,1]])
Y=np.array([[0],[3]])
inv_X=inv(X)
print(Y.shape)
print(inv_X.shape)
W=inv_X.dot(Y)
print(W)

