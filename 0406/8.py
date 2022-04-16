#*headless를 이용하여 웹창없이 실행
#1.네이버 뉴스에 자유검색 검색후 뉴스 제목과 내용 5p 스크래핑하기
#2.csv 파일로 저장
#3.저장된 파일을 이용하여 출력
import time
import csv
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from bs4 import BeautifulSoup
op=webdriver.ChromeOptions()
op.headless=True
op.add_argument("window-size=1920x1080")
op.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
b=webdriver.Chrome(options=op)
b.maximize_window()
b.get("https://naver.com")
print("네이버 접속완료")

title="제목","축약내용"
f=open("savePHJ2.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)

data3=[]
data4=[]
in_data=[]

b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="query"]').send_keys("프로야구\n")
print("네이버 프로야구 검색 완료")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[8]/a').click()
print("네이버 프로야구 검색 후 뉴스 항목 선택 완료")
print("1페이지 정보 저장 중")
b.implicitly_wait(10)
for i in range(2,7):
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    html=b.page_source
    b.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/div/a[{i}]').click()
    if i != 6:
        print(f"{i}페이지클릭 후 정보 저장 중")
    s=BeautifulSoup(html,'html.parser')
    data1=s.select('a.news_tit')
    data2=s.select('a.api_txt_lines.dsc_txt_wrap')
    for i in data1:
        data3.append(i.text)
    for i in data2:
        data4.append(i.text)
    in_data = list(zip(data3, data4))
    time.sleep(1)

writer.writerows(in_data)
print("csv에 저장완료")
f.close()

f=open("savePHJ2.csv","r",encoding="utf-8-sig",newline="")
reader=csv.reader(f)
print("<저장된 csv 값>")
for i in reader:
    print(i)
print("프로그램 종료")