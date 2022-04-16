A=[]
B=[]
C=int(input())
for i in range(C):
    a,b=map(int,input().split(','))
    A.append(a)
    B.append(b)
for i in range(C):
    print(A[i]+B[i])