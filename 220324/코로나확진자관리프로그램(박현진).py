from pickle import dump,load
#코로나확진자관리프로그램
class 코로나:
    확진자_list = []

class 현재확진자수:
    num=0

class 확진자(코로나):
    def __init__(self,이름,나이,거주지역):
        self.__이름=이름
        self.__나이=나이
        self.__거주지역=거주지역
        현재확진자수.num+=1
        print('생성자동작')
    def __del__(self):
        현재확진자수.num-=1
        print('소멸자동작')

    def get_이름(self):
        return self.__이름
    def get_나이(self):
        return self.__나이
    def get_거주지역(self):
        return self.__거주지역

    def __str__(self):
        return f"""이름:{self.__이름}
나이:{self.__나이}
거주지역:{self.__거주지역}
______________________
"""

try:
    i_f=open("save_PHJdata.p","rb")
    코로나.확진자_list=load(i_f)
    i_f.close()
except:
    print("저장된 data가 없습니다.")
    확진자_list=[]
else:
    print("파일을 로드했습니다.")


화면 = f"""{'-' * 10} 코로나확진자관리프로그램 {'-' * 10}
1.  신규확진자등록
2.  확진자명단
3.  확진자확인
4.  연령대별확진자수
5.  지역별확진자수
6.  완지후명단제외
7.  종료 및 저장
{'-' * 43}
실행>>"""

def 신규확진자등록():
    print("확진자등록")
    이름=input("이름:")
    나이=int(input("(만)나이:"))
    거주지역=input("현재거주지역:")
    코로나.확진자_list.append(확진자(이름,나이,거주지역))
def 확진자명단():
    print("<<<확진자명단>>>")
    for i in 코로나.확진자_list:
        print("확진자정보")
        print(i)
def 확진자확인():
    이름=input("이름:")
    for i in 코로나.확진자_list:
        if i.get_이름() == 이름:
            print("확진자정보")
            print(i)
def 연령대별확진자수():
    a=0
    연령대별 = input("연령대를 선택하세요(10대,20대,30대,40대,50대이상):")
    if 연령대별 == "10대":
        for i in 코로나.확진자_list:
            if i.get_나이() >= 10 and i.get_나이() <= 19:
                a+=1
    elif 연령대별 == "20대":
        for i in 코로나.확진자_list:
            if i.get_나이() >= 20 and i.get_나이() <= 29:
                a+=1
    elif 연령대별 == "30대":
        for i in 코로나.확진자_list:
            if i.get_나이() >= 30 and i.get_나이() <= 39:
                a+=1
    elif 연령대별 == "40대":
        for i in 코로나.확진자_list:
            if i.get_나이() >= 40 and i.get_나이() <= 49:
                a+=1
    elif 연령대별 == "50대이상":
        for i in 코로나.확진자_list:
            if i.get_나이() >= 50:
                a+=1
    if a==0:
        print("해당연령대의 확진자는 없습니다.")
    else:
        print("해당연령대의 확진자수:",a,"명")

def 지역별확진자수():
    a=0
    지역별=input("지역을 선택하세요:")
    for i in 코로나.확진자_list:
        if i.get_거주지역() == 지역별:
            a+=1
    if a==0:
        print("해당지역의 확진자는 없습니다.")
    else:
        print("해당지역의 확진자수:",a,"명")

def 완치후명단제외():
    이름=input("완치자 성함:")
    for i in 코로나.확진자_list:
        if i.get_이름() == 이름:
            코로나.확진자_list.remove(i)
            print("입력하신 완치가가 명단에서 제외되었습니다.")

def 종료_및_저장():
    w_f=open("save_PHJdata.p","wb")
    dump(코로나.확진자_list,w_f)
    w_f.close()
    return True

m_d=신규확진자등록,확진자명단,확진자확인,연령대별확진자수,지역별확진자수,완치후명단제외,종료_및_저장
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
        print("현재확진자수:",현재확진자수.num)

