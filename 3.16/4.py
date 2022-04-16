if True:
    print("실행")
if False:
    print("ㅁ실행")
else:
    print("else실행")
#else는 else문장 바로 윗단의 if문으로 인식하고 실행한다.


#입력 1,2,3,4,5
#elif는 무한으로 만들수있지만 권장하지는 않는다.
x=int(input("입력:1~5:"))
if 1==x:
    print("1번길")
elif 2==x:
    print("2번길")
elif 3==x:
    print("3번길")
elif 4==x:
    print("4번길")
elif 5==x:
    print("5번길")
else:
    print("입력된길이없습니다.")




