n=int(input())
for i in range(n):
    N,S=input().split()
    R=int(N)
    for i in range(len(S)):
        print(S[i]*R,end='')
    print()