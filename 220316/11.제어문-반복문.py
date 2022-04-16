#import random
from random import * #외부모듈로 가져와야 rand기능을 사용할수있다.
for i in range(10):
    print(randint(1,100))     #randint은 지정된값사이에서 랜덤한 값을 가져온다.

print()
print(randrange(100))  #randrange은 지정된값사이에서 랜덤한 값을 가져온다.

print()

#up down

정답=randint(1,100) #또는 randrange(1,101)
횟수=1
기록=[]
print("정답:",정답)
입력=int(input("입력:"))
while 입력!=정답:
    기록.append(입력)
    while True:
        if 입력<정답:
            print("Up")
            break
        else:
            print("Down")
            break
    입력 = int(input("입력:"))
    횟수+=1
print(f"{횟수}회째 정답!")
print(f"오답목록:{기록}")





