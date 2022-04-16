import pickle
class 자동차_정보:
    def __init__(self,이름,엔진가격,타이어가격,옵션유무,옵션이름,최고속도,구매가격):
        self.이름 = 이름
        self.엔진가격 = 엔진가격
        self.타이어가격 = 타이어가격
        self.옵션유무 = 옵션유무
        self.옵션이름 = 옵션이름
        self.최고속도 = 최고속도
        self.구매가격 = 구매가격
try:
    data_list = pickle.load(open("save_data.p","rb"))
except:
    data_list = []

max_s = 0
min_s = 1000
run=False
def 입력():
    global max_s,min_s
    name = input("이름 입력 :")
    E_price = int(input("엔진가격 입력 :"))
    T_price = int(input("타이어가격 입력 :"))
    option = input("옵션유무 입력 (있음/없음):")
    if (option == "없음"):
        option_N = "없음"
    else:
        option_N = input("옵션이름 입력 :")
    max_V = int(input("최고속력 입력 :"))
    if (max_V > max_s): max_s = max_V
    if (max_V < min_s): min_s = max_V
    all_price = E_price + T_price
    print(f"구매가격 :{all_price}")
    car_data = 자동차_정보(name, E_price, T_price, option, option_N, max_V, all_price)
    data_list.append(car_data)
    print("차량이 등록되었습니다.")
def 출력():
    if (len(data_list) <= 0):
        print("등록 된 차량이 없습니다.")
    else:
        print("--------------")
        print("차량 목록")
        print("--------------")
        print("이름|타이어가격|엔진가격|옵션유무|옵션이름|최고속도|구매가격")
        for i in data_list:
            print(f"{i.이름},{i.엔진가격},{i.타이어가격},{i.옵션유무},{i.옵션이름},{i.최고속도},{i.구매가격}")
def 가격출력():
    if (len(data_list) <= 0):
        print("등록 된 차량이 없습니다.")
    else:
        print("--------------")
        print("구매가격조회")
        print("--------------")
        print("이름|구매가격")
        for i in data_list:
            print(f"{i.이름},{i.구매가격}")
def 옵션출력():
    if (len(data_list) <= 0):
        print("등록 된 차량이 없습니다.")
    else:
        print("--------------")
        print("차량 목록")
        print("--------------")
        print("이름|타이어가격|엔진가격|옵션유무|옵션이름|최고속도|구매가격")
        for i in data_list:
            if i.옵션유무 != "없음":
                print(f"{i.이름},{i.엔진가격},{i.타이어가격},{i.옵션유무},{i.옵션이름},{i.최고속도},{i.구매가격}")
def 속도확인():
    if (len(data_list) < 2):
        print("2대 이상 등록된 차량이 없습니다.")
        return
    print(f"빠른 자동차와 느린 자동차의 속도차는 {max_s - min_s}입니다.")
def main():
    화면 = """####자동차 정보 프로그램##
    1.자동차 정보 입력
    2.저장된 목록 보기
    3.각 자동차의 구매 가격 조회
    4.옵션이 있는 자동차 정보 조회
    5.빠른 자동차와 느린 자동차의 속도차 조회
    6.프로그램 이용 종료
    #########################
    입력:"""
    매뉴=int(input(화면))
    if 매뉴==1:
        입력()
    elif 매뉴==2:
        출력()
    elif 매뉴 == 3:
        가격출력()
    elif 매뉴 == 4:
        옵션출력()
    elif 매뉴 == 5:
        속도확인()
    elif 매뉴 == 6:
        pickle.dump(data_list,open("save_data.p", "wb"))
        return True
if __name__=="__main__":
    while not run:
        run=main()
