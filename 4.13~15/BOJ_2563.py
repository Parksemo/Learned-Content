array=[]
for i in range(100):
    array.append("o"*100)
    array[i]=list(array[i])
N=int(input())
for i in range(N):
    grade=list(map(int,input().split()))
    for i in range(grade[0],grade[0]+10):
        for j in range(grade[1],grade[1]+10):
            array[i][j]='x'
count=0
for i in range(100):
    for j in range(100):
        if array[i][j]=='x':
            count=count+1
print(count)