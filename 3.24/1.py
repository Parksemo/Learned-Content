l=[1,2,3,4,5]
l2=[7,8,9,12,3]
zip(l,l2) #zip은 같은 인덱스에 있는 값들을 모아서 튜플화한다. <()()()()()>
print(zip(l,l2))     #실제로 출력을 볼수는없다

for i in zip (l,l2):
    print(i)

print(list(zip(l,l2)))