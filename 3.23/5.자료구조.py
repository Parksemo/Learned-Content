s=set([1,2,3,4,5])
s1=set([3,4,5,6,7])
print(s)
s.add(10)
s.update([1,2,3,4])
print(s)
print(s|s1) #합집합
print(s&s1) #교집합
print(s-s1) #차집합