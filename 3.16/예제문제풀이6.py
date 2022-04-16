n=int(input("입력:"))
end=n//100*100 #//와 *의 우선순위는 같고 왼쪽에서 오른쪽으로 계산
print(end)

n=int(((input("입력:"))[:-2])+"00")
print(n)
print(type(n))
