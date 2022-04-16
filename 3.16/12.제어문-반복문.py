#up down 교수가 알려준방식
from random import *

정답=randint(1,100) #또는 randrange(1,101)
횟수=0
기록=[]
print("정답:",정답)

while True:
    횟수 += 1
    입력 = int(input("입력:"))
    if 입력<정답:
        print("Up")
    elif 입력>정답:
        print("Down")
    else:
        print(f"{횟수}회째 정답!")
        print(f"오답목록:{기록}")
        break
    기록.append(입력)
