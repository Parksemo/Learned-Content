class 아이템:
    아이템_list = []


class 인벤토리(아이템):
    def __init__(self,장비,소비,기타):
        self.장비=장비
        self.소비=소비
        self.기타=기타

    def __str__(self):
        return f"""장비:{self.장비}
소비:{self.소비}
기타:{self.기타}
--------------
"""

화면=f"""메이플스토리아이템창열어보기
1.아이템먹기
2.아이템리스트
3.종료
"""

def 아이템먹기():
    print("아이템먹기")
    장비=input("장비:")
    소비=input("소비:")
    기타 = input("기타:")
    아이템.아이템_list.append(인벤토리(장비,소비,기타))

def 아이템리스트():
    print("아이템리스트")
    for i in 아이템.아이템_list:
        print("아이템")
        print(i)

def 종료():
    return True

m_d=아이템먹기,아이템리스트,종료
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


