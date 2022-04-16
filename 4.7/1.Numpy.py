#list
l=[1,2,3,4]
l1=[1,2,3]
l2=[1,2]
al=[l,l1,l2]
print(l+l1)#연결  #크기가 달라도 가능 연결이기때문에
import numpy as np
a=np.array([1,2,3,4])
a1=np.array([1,2,3,4])
a2=np.array([1.,2.,3.,4.])
a3=np.array([1.,2.,3.,4.],int)
#a1=np.array([1,2,3]) # 크기가 같아야 연산이 가능하다
print(a+a1)
print(a+a2)
print(a+a3)
#a4=np.array(1,2,3,4) 하나의값으로 표현해야됨
a4=np.array([1,2,3,4])

