#range() : 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴

#range(시작값=0,종료조건,증감식=1)
print(list(range(10)))

print()

print(list(range(1,10)))
#종료조건은 -1까지 생성된다고 보면됨

print()

print(list(range(1,10,2)))
#1부터 10에 도달할때까지 2씩증가해서 생성됨

print()

#1~10000 간격1 (간격1이면 생략해도되긴함)
print(list(range(1,10001,1)))

print()


#for문 : 정해진 횟수만큼 반복
#whlie:어떤조건이 만족되는 동안, 반복을 계속하는 구조


#for 변수 in 구조:
for i in (1,2,3,4,5):
    print("*")

print()

for i in [1,2,3,4,5]:
    print("*")
#()나 [] 둘다 써도 가능

print()

for i in [1,2,3,4,5]:
    print("*")
    print(i)

print()

x=0
for i in range(10):
    x+=1#0~9
print(x)

x=0
for i in range(10,0,-1):
    x+=1#10~1
print(x)

x=0
for i in range(1,11):
    x+=1#1~10
print(x)

x=0
for i in range(0,10):
    x+=1#0~9
print(x)

print()

for i in [1,2,3,4]:
    print(i)
print(i)
#for문이 종료되면 i값은 보존되며 젤마지막값이 된다.

print()

for i in [1,2,3,4]:
    print(i)
else:
    print("조건종료")
#else는 if에서는 폴스일때 적용되는데 폴문에서는 폴문이 정상적으로 종료될때 적용된다.

print()

#for i in range(정수값이어야함)
l=[1,2,3,4,5,6,7,8,9]
for i in range(len(l)): #range()에서 시작값은0에서 n-1까지이므로 인덱스 번호랑 유용하게 활용가능
    l[i]+=1
print(l)

print()

#추출
l=[1,2,3,4,5,6,7,8,9]
print("[",end="")
for i in l:
    if i==10:
        break #반복탈출 강제탈출 -> else가 적용되지 않는다.
               # else는 정상종료이기때문에 현재 if문에 대한 else는 없어서 상관x
    print(i,end=", ")

else:
    print("]")
    print("정상종료")

print()

l=[1,2,3,4,5,6,7,8,9]
print("[",end="")
for i in l:
    print(i,end=",")
print("\b]") #\b는 한칸을 지우는역할?

print()

for i in range(10):
    print(i,"*"*i) #별의 갯수를 i로 곱한다.

print()

l=[1]*10
print(l)

print()

for i in range(5):
    print(i)
    print("-"*20)
    for i in range(2):
        print(i)

print()

for i in range(5):
    for j in range(2):
        print(i,j)
    print("-")


#두자리수 출력:
#00~99
n=10
for i in range(n):
    for j in range(n):
        print(i,j,sep="")
#n*n
for i in range(1,11):
    for n in range(i):
        print("*",end="")
    print()


print()

#구구단
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}", end="\t") #\t 는 옆으로 쓰는건가?
    print()


print()

#while()문 : 조건이 참인동안 실행할 명령들
#break를 만나면 현재반복문 탈출
#continue를 만나면 처음으로 돌아감

#1~10 5
x=0
while x!=10:
    x+=1
    if x%2==0:
        continue
    print(x)
else:
    print("정상종료")
print(x)

