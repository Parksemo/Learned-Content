x=int(input("0점에서 100점 사이의 점수를 입력하세요.:"))

if 0<=x<=100:
    print(":",x)
    if x >=90:
        print(x,"점은 A학점입니다.")
    elif 80<=x<90:
        print(x, "점은 B학점입니다.")
    elif 70<=x<80:\
        print(x, "점은 C학점입니다.")
    elif 60<=x<70:
        print(x, "점은 D학점입니다.")
    else:
        print(x, "점은 F학점입니다.")

else:
    print("범위를 벗어났습니다.")

