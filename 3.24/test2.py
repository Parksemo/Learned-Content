class A:
    x=10
l=[]
l.append(A())
print(l)
for i in l:
    print(i.x)