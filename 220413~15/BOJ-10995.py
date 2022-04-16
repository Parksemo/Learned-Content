N=int(input())
for i in range(1,N+1):
    if i%2!=0: 
        for i in range(N):
            print(f"* ",end='')
    elif i%2==0:
        for i in range(N):
            print(f" *",end='')    
    print()