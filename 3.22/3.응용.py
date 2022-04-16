def f(x):
    return x
print(f("data"))

(lambda x:x)("data")
print((lambda x:x)("data")) #이함수의 값이 나옴

lambda x:x("data")
print(lambda x:x("data")) #이함수의 주소값이 나옴

(lambda x,y:x+y)("data","출력")
print((lambda x,y:x+y)("data","출력"))

f=lambda x,y:x+y
print(f("a","b"))

l2=[["data",0],["data",10],["data",60],["data",3],["data",1]]
print(sorted(l2))
#sorted는 하나의 키값을 토대로 정렬함
#위에는 [0]값이 동일하여 [1]을 토대로 정렬함

l2=[["data2",0],["data1",10],["data3",60],["data5",3],["data4",1]]
print(sorted(l2))
#이는 [0]값을 토대로 정렬함]

print(sorted(l2,key=lambda x:x[1]))
#key=lambda를 통해 키값을 설정하여 [1]값을 기준으로 정렬함

