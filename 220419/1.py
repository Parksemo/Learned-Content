import numpy as np
from numpy.linalg import inv #역행렬
a=np.array([2,1])
print(a) #백터 선
print(np.linalg.norm(a)) #선 길이 피타고라스처럼
행렬1=np.array([[1,2],[3,4]]) #행렬 면
print(행렬1)
m1=np.array([[1,2],[3,4]])
m2=np.array([[1,2],[3,4]])
print(m1*m2)
print(m1+m2)
i_m1=inv(m1) #역행렬
print(m1)
print(i_m1)
print(np.dot(m1,m2)) #내적
x=np.array([1,2,3])
y=np.array([4,5,6])
print(np.dot(x,y))
m_x=np.array([[1,2,3]])
m_y=np.array([[4,5,6]])
print(m_x)
print(m_y)
m_y=m_y.T #행렬의 전치
print(m_x.shape)
print(m_y.shape)
print(np.dot(m_x,m_y))
print(m_x.dot(m_y)) #위와 동일
a1=[[1,2,3],[-1,-2,-3]]
a2=[[4,-4],[5,-5],[6,-6]]
y=np.dot(a1,a2)
print(y)
A=[[1,2,3],[4,5,6],[7,8,9]]
i_A=inv(A)
print(i_A)