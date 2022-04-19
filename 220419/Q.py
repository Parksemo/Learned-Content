import numpy as np
from numpy.linalg import inv
X=np.array([[2,3],[1,-2]])
Y=np.array([[1],[4]])
inv_X=inv(X)
W=inv_X.dot(Y)
print(W)