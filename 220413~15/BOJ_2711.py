T=int(input())

for i in range(T):
    n,b=input().split()
    a=int(n)
    b=list(b)
    b.pop(a-1)
    for i in b:
        print(i,end='')
    print()