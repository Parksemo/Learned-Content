from pykiwoom.kiwoom import *
import time
import pandas as pd


#로그인
kiwoom = Kiwoom()
print("로그인중")
kiwoom.CommConnect(block=True)
print(("로그인 완료"))


#연결
state = kiwoom.GetConnectState()
if state == 0:
    print('연결되지않음')
elif state == 1:
    print("연결됨")


#로그인정보
account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부
# print(account_num)
# print(accounts)
# print(user_id)
# print(user_name)
# print(keyboard)
# print(firewall)

corp = kiwoom.GetMasterCodeName('035720')
print(f"기업 : {corp}")
df_single = kiwoom.block_request('opt10001',
                                 종목코드 = '035720',
                                 output = '주식기본정보',
                                 next=0
                                 )
df_single