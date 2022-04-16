A,B=input().split()
a=[]
b=[]
c=0
d=0
for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            a.append(i)
            b.append(j)
c=int(a[0])
d=int(b[0])
for k in range(len(B)):
    if k==d:
        print(A)
    else:
        print(f"{'.'*c}{B[k]}{'.'*(len(A)-c-1)}")