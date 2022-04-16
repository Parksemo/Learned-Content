array=[]
count=0
for i in range(8):
    array.append(input())
    array[i]=list(array[i])
for i in range(8):
    for j in range(8):
        if i%2==0:
            if j%2==0:
                if array[i][j]=='F':
                    count=count+1
        if i%2!=0:
            if j%2!=0:
                if array[i][j]=='F':
                    count=count+1
print(count)