#저장방식 설정
#고객계좌=dict.fromkeys(["고객명","계좌번호","초기금액"],None)
은행계좌내역={}
#계좌생성
def 계좌생성():
    고객계좌={}
    고객계좌["고객명"]=input("고객명:")
    고객계좌["계좌번호"]=input("계좌번호:")
    고객계좌["초기금액"]=int(input("금액:"))
    은행계좌내역[고객계좌["계좌번호"]]=고객계좌

#입금
def 입금():
    계좌번호=input("입금할 계좌번호:")
    if 계좌번호 not in 은행계좌내역.keys():
        print("선택하신 계좌가 없습니다.")
        return
    입금금액=int(input("입금금액:"))
    은행계좌내역[계좌번호]["초기금액"]+=입금금액

#출금
def 출금():
    계좌번호=input("출금할 계좌번호:")
    if 계좌번호 not in 은행계좌내역.keys():
        print("선택하신 계좌가 없습니다.")
        return
    출금금액=int(input("출금금액:"))
    if 은행계좌내역[계좌번호]["초기금액"]<출금금액:
        print("잔액부족")
        return
    은행계좌내역[계좌번호]["초기금액"]-=출금금액
#고객정보출력
def 고객정보출력():
    print(은행계좌내역)

#종료
def 종료():
    return True

run_v=False
while not run_v:
    print("은행프로그램")
    print("1.계좌생성")
    print("2.입금")
    print("3.출금")
    print("4.고객정보출력")
    print("5.종료")
    m=input("메뉴")
    if m=='1':
        계좌생성()
    elif m=='2':
        입금()
    elif m=='3':
        출금()
    elif m=='4':
        고객정보출력()
    elif m=='5':
        run_v=종료()
    else:print("잘못입력")




