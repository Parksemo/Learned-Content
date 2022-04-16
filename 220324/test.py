import pickle
class 스토어:
    검색기록=[]
    ID_LIST=[]
class 개인정보(스토어):
    def __init__(self,ID,현재자금):
        self.__ID=ID
        self.__현재자금=현재자금

    def get_ID(self):
        return self.__ID

    def __str__(self):
        return f"""ID:{self.__ID}
현재자금:{self.__현재자금}
______________________
"""

class 검색(스토어):
    def __init__(self,검색목록):
        self.검색목록=검색목록




화면=f"""
>~~~~~~~~~~<   천냥할인 스토어    >~~~~~~~~~~
1.  ID로그인
2.  스토어검색
3.   검색기록
4.   구매목록체크
5.   구매 및 현재자금
6.   종료
>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<
"""
def ID로그인():
    print("ID정보를 입력해주세요.")
    ID=input("ID:")
    현재자금=int(input("현재자금:"))
    스토어.ID_LIST.append(개인정보(ID,현재자금))
    print("로그인 성공하셨습니다.")

def 스토어검색():
    print("검색정보를 입력해주세요.")
    검색하기 = input("검색:")
    스토어.검색기록.append(검색(검색하기))

def 검색기록():
    ID검색기록=input("id검색기록)")
    for i in 스토어.ID_LIST:
        if i.get_ID() == ID검색기록:
            print("검색한ID정보")
            print(i)

def 구매목록체크():
    pass
def 구매_및_현재자금():
    pass


def 종료():
    print("종료하겠습니다.")
    return True

def main():
    m=ID로그인,스토어검색,검색기록,구매목록체크,구매_및_현재자금,종료
    m_i = int(input(화면))
    if m_i not in range(1, len(m) + 1):
        print("잘못입력되었습니다.")
        return
    return m[m_i-1]()

if __name__=="__main__":
    run=False
    while not run:
        run=main()