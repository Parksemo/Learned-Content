C=int(input())
for i in range(C):
    class_average=0
    percent=0
    count=0
    grade=list(map(int,input().split()))
    class_average=sum(grade[1:])/grade[0]
    for j in range(1,grade[0]+1):
        if class_average < grade[j]:
            count=count+1
    percent=count/grade[0]*100
    print(f"{percent:.3f}%")