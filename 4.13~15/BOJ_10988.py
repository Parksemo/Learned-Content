a=input()
b=0
N=len(a)
for i in range(N):
    if a[i]==a[N-1-i]:
        b+=1
if N==b:
    print("1")
else:
    print("0")