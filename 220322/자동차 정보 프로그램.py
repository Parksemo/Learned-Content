"""
class data:
    def __init__(self):
        self.data1=0
        self.data2 = 0
        self.data3 = 0
        self.data4 = 0
        self.data5 = 0
        self.data6 = 0
        self.data7 = 0

    def __str__(self):
        return f"{self.data1}{self.data2}{self.data3}{self.data4}{self.data5}{self.data6}{self.data7}"

    def __repr__(self):
        return f"{self.data1}{self.data2}{self.data3}{self.data4}{self.data5}{self.data6}{self.data7}"

print(data())
l=[data(),data()]
print(l)

"""

class 자동차:
    def __init__(self):
        self.이름=""
        self.엔진가격 = 0
        self.타이어가격 = 0
        self.옵션 = ""
        self.옵션이름 = ""
        self.최고속도 = 0
        self.구매가격 = 0

class 슈퍼카(자동차):
    def __init__(self):
        self.이름="슈퍼카"
        self.엔진가격 = 900
        self.타이어가격 = 500
        self.옵션 = "있음"
        self.옵션이름 = "썬루프"
        self.최고속도 = 300
        self.구매가격 = int(self.엔진가격)+int(self.타이어가격)

    def __str__(self):
        return f"이름:{self.이름} 엔진가격:{self.엔진가격} 타이어가격:{self.타이어가격} 옵션:{self.옵션} 옵션이름:{self.옵션이름} 최고속도:{self.최고속도} 구매가격:{self.구매가격}"

class 고물차(자동차):
    def __init__(self):
        self.이름="고물차"
        self.엔진가격 = 473
        self.타이어가격 = 365
        self.옵션 = "없음"
        self.옵션이름 = "없음"
        self.최고속도 = 23
        self.구매가격 = int(self.엔진가격)+int(self.타이어가격)

    def __str__(self):
        return f"이름:{self.이름} 엔진가격:{self.엔진가격} 타이어가격:{self.타이어가격} 옵션:{self.옵션} 옵션이름:{self.옵션이름} 최고속도:{self.최고속도} 구매가격:{self.구매가격}"



print("#### 자동차 정보 프로그램 ####")

while True:
    x = int(input("번호입력:"))
    if x == 1:
        x1 = input("1.자동차 정보 입력:")


    elif x == 2:
        print("2.저장된 목록 보기")

        if x1 == "슈퍼카":
            a = 슈퍼카()
            print(a)
        elif x1 == "고물차":
            a = 고물차()
            print(a)
        else:
            print("입력하신 자동차 정보는 없습니다.")



    elif x == 3:
        print("3.각 자동차의 구매 가격 조회")
        a=슈퍼카()
        b=고물차()
        print(f"슈퍼카의 구매가격:{a.구매가격}")
        print(f"고물차의 구매가격:{b.구매가격}")

    elif x == 4:
        print("4.옵션이 있는 자동차 정보 조회")
        a = 슈퍼카()
        b = 고물차()
        if a.옵션 == "있음":
            print(a)
        elif b.옵션 == "있음":
            print(b)

    elif x == 5:
        print("4.빠른 자동차와 느린 자동차의 속도차 조회")
        a = 슈퍼카()
        b = 고물차()
        if a.최고속도 > b.최고속도:
            print(f"빠른자동차:{a.이름},속도:{a.최고속도}")
            print(f"느린자동차:{b.이름},속도:{b.최고속도}")
            print(f"속도차:{int(a.최고속도)-int(b.최고속도)}")
        elif a.최고속도 < b.최고속도:
            print(f"빠른자동차:{b.이름},속도:{b.최고속도}")
            print(f"느린자동차:{a.이름},속도:{a.최고속도}")
            print(f"속도차:{int(b.최고속도) - int(a.최고속도)}")
        else:
            print("두 자동차의 속도가 동일합니다.")

    elif x == 6:
        print("프로그램 이용 종료")
        break










