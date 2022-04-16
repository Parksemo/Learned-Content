from collections import deque
l=deque()
l=[]
l.append(10)
l.append(20)
l.append(30)
print(l)
print(l.pop())
print(l)

print()

l=[]
l.append(10)
l.append(20)
l.append(30)
l.pop(0)

l1=list("data")
print(l1)
l2=deque("data")
l2.append("10")
print(l2)
l2.appendleft("10")
print(l2)
l2.extend("10")
print(l2)
l2.extendleft("10")
print(l2)

#스택은 선입후출이며 입구가 하나라서 역순으로 뽑을려고할때 사용하고
#큐는 선입선출이며 입구와 출구 두개라서 입력한 순서대로 뽑을려고할때 사용한다


