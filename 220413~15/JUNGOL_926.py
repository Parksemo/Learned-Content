first_array=[]
second_array=[]
mul_array=[]
first=input()
if first=='first array':
    for i in range(2):
        first_array.append(list(map(int,input().split())))
second=input()
if second=='second array':
    for i in range(2):
        second_array.append(list(map(int,input().split())))

for i in range(2):
    for j in range(4):
        mul_array.append(first_array[i][j]*second_array[i][j])
for i in range(4):
    print(f"{mul_array[i]} ",end='')
print()
for i in range(4,8):
    print(f"{mul_array[i]} ",end='')