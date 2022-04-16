import time
import csv
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from bs4 import BeautifulSoup

title="동화명","심볼","현재가","전일대비","등락율"
f=open("savePHJ.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
data4=[]
data5=[]
data6=[]
data7=[]
data8=[]
data9=[]
data10=[]
in_data=[]

b=webdriver.Chrome()
b.implicitly_wait(10)
b.get("https://naver.com")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="query"]').send_keys("금융\n")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="web_1"]/div/div[2]/div[2]/a').click()
b.switch_to.window(b.window_handles[1])
time.sleep(1)
b.find_element_by_xpath('//*[@id="menu"]/ul/li[4]/a').click()
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="tab_section"]/ul/li[2]/a').click()
b.implicitly_wait(10)
b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
b.switch_to.frame("frame_ex2")#내부에 또다른 html이 있을때에는 전환이 필요하다.

#리스트에 저장
for i in range(2,6):
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    b.implicitly_wait(10)
    html=b.page_source
    b.implicitly_wait(10)
    if i !=5:
        b.find_element_by_xpath(f'/html/body/div/div/a[{i}]').click()
        b.implicitly_wait(10)
    s=BeautifulSoup(html,'html.parser')
    b.implicitly_wait(10)
    data1=s.find_all('td',attrs={"class":"tit"})
    b.implicitly_wait(10)
    data2=s.find_all('td',attrs={"class":"symbol"})
    b.implicitly_wait(10)
    data3=s.find_all('td',attrs={"class":"num"})
    b.implicitly_wait(10)
    for i in data1:
        data4.append(i.a.text)
    for i in data2:
        data5.append(i.a.text)
    for i in data3:
        data6.append(i.text.strip())
    time.sleep(1)

#현재가,전일대비,등락율 분리
for i in range(len(data6)//3):
    data7.append(data6[i*3])
    data8.append(data6[i*3+1])
    data9.append(data6[i*3+2])
for i in range(len(data9)):
    if data9[i][0]=="-":
        data10.append(data9[i].replace("\n\t\t\t\t\t\t ",""))
    elif data9[i][0]=="+":
        data10.append(data9[i].replace("\n\t\t\t\t\t\t\n\t\t\t\t\t\t",""))
    else:
        data10.append(data9[i])

#csv저장
in_data = list(zip(data4,data5,data7,data8,data10))
writer.writerows(in_data)
f.close()
f=open("savePHJ.csv","r",encoding="utf-8-sig",newline="")
reader=csv.reader(f)
for i in reader:
    print(i)
