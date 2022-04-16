import requests
from bs4 import BeautifulSoup
url=("https://finance.naver.com/sise/sise_rise.naver?sosok=1")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

data1=soup.select("a.tltle")
data2=soup.select("td.number")



for j in range(0,len(data1)):
    for i in data1[j]:
        print("종목명 :",i.text.strip(),end=",  ")
    for i in data2[j*10]:
        print("현재가 :",i.text.strip(),end=",  ")
    for i in data2[j*10+3]:
        print("거래량 :",i.text.strip(),end=",  ")
    for i in data2[j*10+4]:
        print("매수호가 :",i.text.strip(),end=",  ")
    for i in data2[j*10+5]:
        print("매도호가 :",i.text.strip(),end=",  ")
    for i in data2[j*10+6]:
        print("매수총잔량 :",i.text.strip(),end=",  ")
    for i in data2[j*10+7]:
        print("매도총잔량 :",i.text.strip(),end=",  ")
    for i in data2[j*10+8]:
        print("PER :",i.text.strip(),end=",  ")
    for i in data2[j*10+9]:
        print("ROE :",i.text.strip())
    print()


