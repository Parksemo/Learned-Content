#딕셔너리는 순서가 없다 주머니형식
#인덱스가 없다
#값은 중복될 수 있지만, 키값은 중복될수없으면 이는 마지막값으로 된다.
dic={}
print(type(dic))

print()

dic={"key1":10,"key1":20}
print(dic)
print(dic["key1"])
#딕셔너리는 인덱스는 없지만 키가 인덱스의 역할을 할 수 있다.


print()


l=[1,2]
l[0]=20
print(l)
dic={"key1":10,"key1":20}
dic["key1"]=100
print(dic)
#리스트에서 특정 인덱스위치에 값을 바꿔줄수있듯이
#딕셔너리도 키를통해 특정키의 값을 바꿔줄수있다.


print()

d=dict(k=10) #k는 식별자로서 식별자규칙처럼 맨앞에 숫자가위치하면안된다.
print(d)


print()


d={0:1,1:2,2:3}
print(d)
print(d[0])
