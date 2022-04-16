#1.네이버 뉴스에 암호화폐 검색후 뉴스 제목과 내용 5p 스크래핑하기
#2.csv 파일로 저장
#3.저장된 파일을 이용하여 출력
import time
import csv
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from bs4 import BeautifulSoup
title="제목","축약 내용"
f=open("savePHJ.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
data3=[]
data4=[]
in_data=[]

b=webdriver.Chrome()
b.implicitly_wait(10)
b.get("https://naver.com")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="query"]').send_keys("암호화폐\n")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
b.implicitly_wait(10)
for i in range(2,7):
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    html=b.page_source
    b.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/div/a[{i}]').click()
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

f.close()

f=open("savePHJ.csv","r",encoding="utf-8-sig",newline="")
reader=csv.reader(f)
for i in reader:
    print(i)
