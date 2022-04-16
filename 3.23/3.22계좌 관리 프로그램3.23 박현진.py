import pickle

class 은행:
    은행계좌정보={}
    def __init__(self,계좌번호,계좌주,초기입금):
        self.계좌번호=계좌번호
        self.계좌주=계좌주
        self.초기입금=초기입금
        self.내역=f"초기입금:{초기입금}|합계금액{초기입금}|\n"

    def 내역기록(self,입력):
        if 입력>0:
            self.내역 += f"입금{입력}|합계금액{self.초기입금}|\n"
        else:
            입력 *=-1
            self.내역 += f"출금{입력}|합계금액{self.초기입금}|\n"
try:
    은행.은행계좌정보 = pickle.load(open("save_Cdata.p","rb"))
except:
    은행.은행계좌정보 = {}

def 생성():
    print("""--------------
계좌생성
--------------
""")
    계좌번호=input("계좌번호:")
    if 계좌번호 in 은행.은행계좌정보:
        print("이미 등록된 계좌번호입니다.")
    else:
        계좌주 = input("계좌주:")
        초기입금 = int(input("초기입금액:"))
        은행.은행계좌정보[계좌번호]=은행(계좌번호,계좌주,초기입금)
def 목록():
    print("""--------------
계좌목록
--------------
""")
    print("계좌번호|계좌주|예금액")
    for i in 은행.은행계좌정보.values():
        print(i.계좌번호,end="|")
        print(i.계좌주,end="|")
        print(i.초기입금)
def 입금():
    print("""--------------
예금
--------------
""")
    계좌번호 = input("계좌번호:")
    if 계좌번호 not in 은행.은행계좌정보:
        print("등록된 계좌가 없습니다.")
        return
    확인계좌=은행.은행계좌정보[계좌번호]
    예금액=int(input("예금액:"))
    확인계좌.초기입금+=예금액
    확인계좌.내역기록(예금액)
    print("예금성공")
def 출금():
    print("""--------------
출금
--------------
""")
    계좌번호 = input("계좌번호:")
    if 계좌번호 not in 은행.은행계좌정보:
        print("등록된 계좌가 없습니다.")
        return
    확인계좌 = 은행.은행계좌정보[계좌번호]
    출금액 = int(input("출금액:"))
    try:
        if 확인계좌.초기입금 < 출금액:
            int("a")
        확인계좌.초기입금 -= 출금액
        출금액 *= -1
        확인계좌.내역기록(출금액)
        print("출금성공")
    except:
        print("잔고가 부족합니다.")


def 종료():
    print("프로그램 종료")
    pickle.dump(은행.은행계좌정보, open("save_Cdata.p", "wb"))
    return True
def 송금():
    print("""--------------
송금
--------------
""")
    입금계좌번호 = input("입금 계좌번호:")
    if 입금계좌번호 not in 은행.은행계좌정보:
        print("등록된 계좌가 없습니다.")
        return
    출금계좌번호 = input("출금 계좌번호:")
    if 출금계좌번호 not in 은행.은행계좌정보:
        print("등록된 계좌가 없습니다.")
        return
    출금계좌 = 은행.은행계좌정보[출금계좌번호]
    출금액 = int(input("출금액:"))
    if 출금계좌.초기입금 < 출금액:
        print("잔고가 부족합니다.")
        return

    try:
        if 출금계좌.초기입금 < 출금액:
            int("a")
        출금계좌.초기입금 -= 출금액
        출금액 *= -1
        출금계좌.내역기록(출금액)
        예금액 = 출금액 * (-1)
        입금계좌 = 은행.은행계좌정보[입금계좌번호]
        입금계좌.초기입금 += 예금액
        입금계좌.내역기록(예금액)
        print("송금완료")
    except:
        print("잔고가 부족합니다.")

def 내역():
    print("""--------------
내역조회
--------------
""")
    계좌번호 = input("계좌번호:")
    if 계좌번호 not in 은행.은행계좌정보:
        print("등록된 계좌가 없습니다.")
        return
    print(은행.은행계좌정보[계좌번호].내역)
run=False
m=생성,목록,입금,출금,종료,송금,내역
while not run:
    idx=int(input("""----------------------------------------------------------
1.계좌생성 | 2.계좌목록 | 3.예금 | 4.출금 | 5.종료 | 6.송금 | 7.내역조회
----------------------------------------------------------
선택> """))
    if idx not in range(1,len(m)+1):
        print("잘못입력되었습니다.")
        continue
    run=m[idx-1]()


