#리스트는 값이 순서가 있음 왼쪽에서 오른쪽
#append는 끝에 값의 부여
l=[]
l.append(1)
print(l)
l.append(2)
print(l)
l.append("data")
print(l)
l.append([1,2,3,4,5])
print(l)


print()

#extend는 리스트끝에 리스트튜플딕트값을 하나씩 추가한다.
l=[]
l.extend("1234")
print(l)
#extend는 반드시 감싸져있는 덩어리값을 사용한다?
#그 덩어리값을 하나씩 나눠서 추가한다


#insert는 내가 원하는 장소에 추가
l=[1,2,3,4,5]
print(len(l))
l.insert(1,10)
print(l)#그자리에 값이 추가되면서 밀리는 것이지 그 위치값이 사라지는것은 아니다
#l[1]=10을하게된다면 2의값이 10으로 변경되며 밀리지않고 그위치값이 사라진다.
print(len(l))

print()


#pop([idx])
#pop은 젤 마지막 값을 꺼낸다, 인덱스번호를 부여하면 그위치의 값을 꺼낸다.
#꺼내는것이기에 그 값은 존재한다.
l=[1,2,3,4,5]
print(l.pop())
print(l)

l=[1,2,3,4,5]
print(l.pop(1))
print(l)

print()

#remove는 해당되는 값을 찾아 삭제하는것이다.
#삭제하기 때문에 그값은 존재하지 않는다.
l=[1,2,3,4,5]
print(l.remove(1))
print(l)

print()

#clear는 ~?
l=[1,2,3,4,5]
l.clear()
print(l)

print()

#count는 해당하는 값이 몇개가 존재하는지
l=[1,2,3,4,5]
print(l.count(3))


print()

#index는 해당하는 값의 인덱스번호를 알려준다.
l=[1,2,3,4,5]
print(l.index(3))

print()


l=[1,2,3,4,5,6,7,8,9,10]
l.reverse()
print(l)
#reverse는 값들의 방향을 바꿔주는것으로
# 슬라이싱과 차이점은 슬라이싱은 기존의 값이 바뀌지않고 리버스는 바뀐다.
l=[1,2,3,4,5,6,7,8,9,10]
l=l[::-1]
print(l) #이렇게 l에 대입을 하면 리버스처럼 기존값이 바뀔수잇다.


print()

#sorted는 값을 오름차순으로 정렬한다. 기존의 값이 유지되어 기존의 값은 정렬되지않는다.
l=[1,9,8,4,5,18,7,42,9,51]
print(sorted(l))
print(l)

print()

#sort는 sorted와 마찬가지로 값을 오름차순으로 정렬하는데 기존의 값이 정렬된 값으로 바뀐다.
l=[1,9,8,4,5,18,7,42,9,51]
print(l.sort())
print(l)


