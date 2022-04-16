#1. 네이버 뉴스 과학기사 수집 (제목, 축약 내용)
#2. 연속적 페이지 전환으로 수집 단 sleep(5)

import time
import csv
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
url=("https://news.naver.com/main/list.naver?mode=LS2D&sid2=228&sid1=105&mid=shm&date=20220404&page=")

title="제목","축약 내용"
f=open("save3.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
in_data=[]

for page in range (1,6):
    print(f"page{page} 크롤링중")
    r=requests.get(url+str(page),headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")
    data=soup.find_all("dl")
    for i in data:
        if i.a:
            in_data.append([i.dd.previous_sibling.previous_sibling.text.strip(),i.span.text.strip()])
    time.sleep(5)

writer.writerow(in_data)


