#1. https://land.naver.com/news/region.naver?city_no=4800000000&dvsn_no=&page=1
# 에서 뉴스 5페이지 수집하고 저장
#time slepp에서 randint(3,6)사용
#2. 개인에게 맞는 User-Agent 정보를 찾아서 헤더를 이용하여 접속
#3. csv파일로 저장
#4. 뉴스의 제목,내용 2가지를 이용하여 입력
#5. 저장된 csv파일을 이용하여 내용 출력!


import time
import csv
import requests
from bs4 import BeautifulSoup
from random import randint
url=("https://land.naver.com/news/region.naver?city_no=4800000000&dvsn_no=&page=")

title="제목","축약 내용"
f=open("save1.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
in_data=[]
data3=[]
data4=[]

for page in range (1,6):
    print(f"page{page} 크롤링중")
    r=requests.get(url+str(page))
    soup=BeautifulSoup(r.text,"html.parser")
    data1 = soup.find_all("dl")
    data2 = soup.find_all("dd")
    for i in data1:
        if i.a:
            data3.append(i.dd.previous_sibling.previous_sibling.text.strip())
    for i in data2:
        if i.span:
            data4.append(i.span.previous_sibling.text.strip())
    in_data=list(zip(data3,data4))
    p = randint(3, 6)
    print("이번 크롤링 시간:",p,"초")
    time.sleep(p)
    print("크롤링 완료")

writer.writerows(in_data)
f.close()

f=open("save1.csv","r",encoding="utf-8-sig",newline="")
reader=csv.reader(f)
for i in reader:
    print(i)
