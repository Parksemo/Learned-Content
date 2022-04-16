T=int(input())
d=[]
for i in range(T):
    a=[]
    b=[]
    c=[]
    k=int(input())
    for j in range(k):
        a.append(input())
    for o in range(k):
        for p in range(k):
            if o!=(k-p-1):
                b.append(a[o]+a[k-p-1])
    for s in range(len(b)):
        if b[s]==b[s][::-1]:
            c.append(b[s])
    if len(c)==0:
        d.append('0')
    elif len(c)!=0:
        d.append(c[0])

for v in range(T):     
        print(d[v])