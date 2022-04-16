class 계좌:
    def __init__(self):
        self.계좌번호=""
        self.계좌주 = ""
        self.초기입금액 = 0
        self.예금액 = 0
        self.출금액 = 0
        self.현재금액 = 0

class 계좌생성(계좌):
    def __init__(self,계좌번호,계좌주,초기입금액,예금액,출금액):
        self.계좌번호 = 계좌번호
        self.계좌주 = 계좌주
        self.초기입금액 = 초기입금액
        self.예금액 = 예금액
        self.출금액 = 출금액
        self.현재금액 = self.초기입금액+self.예금액-self.출금액

    def __str__(self):
        return f"{self.계좌번호}    {self.계좌주}    {self.현재금액}"

while True:
    print("-" * 50)
    print("1.계좌생성 | 2.계좌목록 | 3.예금 | 4.출금 | 5.종료")
    print("-" * 50)
    x=int(input("선택> "))
    if x == 1:
        print("-" * 10)
        print("계좌생성")
        print("-" * 10)

        x1=input("계좌번호:")
        x2=input("계좌주:")
        x3=int(input("초기입금액:"))
        x4=0
        x5=0
        x6=x3
        a = 계좌생성(x1,x2,x3,x4,x5)
        a.현재금액 = x6
        print("결과: 계좌가 생성 되었습니다.")

    elif x == 2:
        print("-" * 10)
        print("계좌목록")
        print("-" * 10)
        a = 계좌생성(x1,x2,x3,0,0)
        a.현재금액 = x6
        print(a)

    elif x == 3:
        print("-" * 10)
        print("예금")
        print("-" * 10)
        print(f"계좌번호:{a.계좌번호}")
        x4=int(input("예금액:"))
        x5 = 0
        a = 계좌생성(x1, x2, x3, x4, x5)
        x6=int(x6)+int(x4)
        a.현재금액=x6

    elif x == 4:
        print("-" * 10)
        print("출금")
        print("-" * 10)
        print(f"계좌번호:{a.계좌번호}")
        x5=int(input("출금액:"))
        x4=0
        a = 계좌생성(x1, x2, x3, x4, x5)
        x6=int(x6)-int(x5)
        a.현재금액=x6

    elif x ==5:
        print("프로그램 종료")
        break

    else:
        print("1~5번값을 입력하세요")
        continue



