# 결론 : ==는 같은 값을 가지는지 확인
#       is는 같은 객체이며 같은 주소를 가지는지 확인

l=[1,2,3,4,5]
l2=[1,2,3,4,5]
print(id(l),id(l2)) #두 리스트의 내부 값은 동일하지만 주소는 다르다.
print(l==l2) #값은 같다.
print(l is l2) #같은 값을 가지지만 다른 주소를 가지며 다른 객체이다.

print()

tp=(1,2,3,4,5)
tp2=(1,2,3,4,5)
print(id(tp),id(tp2)) #이는 값도 동일하고 주소도 동일하게 나온다.
print(tp==tp2) #값동일
print(tp is tp2) #주소동일
#이는 최신버전인 파이튜터에서 하면 주소가 다르게 나온다. 파이참에서 주소가
# 다르게 나오려고 하려면 아래와 같이 부여하면 절대적으로 생성하여 다른 주소가 된다.
# 그렇지만 이 경우는 새로운 메모리 공간을 할당하기에 효율적이진 못하다

print()

tp=tuple[(1,2,3,4,5)]
tp2=tuple[(1,2,3,4,5)]
print(id(tp),id(tp2))

print()

l=list[1,2,3,4,5]
l2=list[1,2,3,4,5]
print(id(l),id(l2))



print()


l=[1,2,3]
l2=l
l[1]=10
print(l)
print(l2)
#이는 리스트가 뮤터블로써 l2가 l과 같은 값을 가지고 l의 값을 바꿔줘도 l2도 같이 바뀐다?


print()


#참조하지않는 객체:가비지컬렉터
l=[1,2,3]
l2=l
l3=l[:] #슬라이싱을 통해 l3는 l와 다른 생성된 값을 가진다.
del(l)
#이렇게 되면 l은 사라지지만 l이 참조하고있던 값은 사라지는것이 아니다.


#딕셔너리에서 키값은 고유해서 바뀌지 않지만 밸류값은 바뀔수있다.


print()


d={"data":10,1:20}
d.update(k=10) #업데이트 사용시 여기서 k는 키값으로 식별자이며 첫글자 숫자x
#식별자로 전달하는 것은 문자열로 된다.
d["data"]=100
print(d)

print()

d.update(k=20, key=20) #k라는 키값이 존재하기에 그 밸류값을 변경한다.
print(d)

print()

d2=d.fromkeys((1,2,3),[1,2,3]) #리스나 튜플의 값들을 가져온다 왼쪽은 키값이 되고
# 오른쪽은 밸류값이 된다.
d3=d.fromkeys((1,2,3),1)
print(d)
print(d2)
print(d3)

print()
print(d.get(1)) #get은 해당 키의 밸류값을 얻을수있는것으로
#pop과 같이 새로 형성되는 것은 동일하지만 pop은 기존의 형태가 바뀌지만 get은 그대로이다.

print()
print(d)
print(d.keys()) #키값
print(d.values()) #밸류값
print(d.items())
print(list(d.items()))
l2=list(d.items())
l2[0][0] #이름과 젤 가까울수록 고차원인덱스, 멀수록 저차원인덱스가된다.
print(l2[0][0])
print(l2[0][1])
print(l2[1][0])
print(l2[1][1])

print()
print(d)
print(d.pop(1)) #해당키의 값을 꺼낸다
print(d)
print(d.popitem()) #젤 마지막 키와 밸류값을 튜플형식으로 꺼낸다.
print(d)


#del과 clear의 차이점은 del은 아예없애는것이고 clear는 비우는것이다.






















