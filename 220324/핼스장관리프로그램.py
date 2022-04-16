from pickle import dump,load

#헬스장 관리프로그램
"""
핵심 기술:클래스,파일입출력,예외처리
프로그램 개요: 핼스장관리프로그램 (회원정보등록,기구관리,고객확인,남은기간)
언어/기술: python/클래스, 파일입출력, 예외처리
설계및화면: [설계] 1.회원정보등록 2.기구관리 3.고객확인 4,남은기간
"""
class 핼스장:
    고객_list=[]
    기구정보=[]

class 회원정보(핼스장):
    def __init__(self,이름,번호,기간):
        self.__이름=이름
        self.__번호=번호
        self.__기간=기간
    def get_이름(self):
        return self.__이름
    def __str__(self):
        return f"""이름:{self.__이름}
번호:{self.__번호}
잔여 기간:{self.__기간}
______________________
"""
    def 기간출력(self):
        return f"이름:{self.__이름} 잔여기간:{self.__기간}"

try:
    i_f=open("save_data.p","rb")
    핼스장.고객_list=load(i_f)
    핼스장.기구정보=load(i_f)
    i_f.close()
except:
    print("저장된 data가 없습니다.")
    고객_list=[]
    기구정보=[]
else:
    print("파일을 로드했습니다.")

화면 = f"""{'-' * 10} 관리프로그램 {'-' * 10}
1.  회원정보등록
2.  기구확인
3.  기구추가
4.  고객확인
5.  남은 기간
6.  종료 및 저장
{'-' * 34}
실행>>"""

def 회원정보등록():
    print("회원등록")
    이름=input("이름:")
    입력=input("휴대폰 번호입력'-'생략, 번호만 입력")
    번호=입력[:3]+"-"+입력[3:7]+"-"+입력[7:]
    기간=int(input("등록기간:"))
    핼스장.고객_list.append(회원정보(이름,번호,기간))
def 기구확인():
    print(핼스장.기구정보)
def 기구추가():
    x=input("추가기구명")
    핼스장.기구정보.append(x)
def 고객확인():
    이름=input("이름:")
    for i in 핼스장.고객_list:
        if i.get_이름() == 이름:
            print("고객정보")
            print(i)
def 남은_기간():
    print("헬스장의 모든 고객 잔여시간 출력")
    for i in 핼스장.고객_list:
        print(i.기간출력())
def 종료_및_저장():
    w_f=open("save_data.p","wb")
    dump(핼스장.고객_list,w_f)
    dump(핼스장.기구정보,w_f)
    w_f.close()
    return True
m_d=회원정보등록,기구확인,기구추가,고객확인,남은_기간,종료_및_저장
def main():
    m=int(input(화면))
    if m not in range(1,len(m_d)+1):
        print("잘못입력되었습니다.")
        return
    return m_d[m-1]()

if __name__=="__main__":
    run=False
    while not run:
        run=main()

    """
    if m==1:
        회원정보등록()
    elif m==2:
        기구확인()
    elif m==3:
        기구추가()
    elif m==4:
        고객확인()
    elif m==5:
        남은_기간()
    elif m==6:
        return True
    else:
        print("잘못입력되었습니다.")
"""


