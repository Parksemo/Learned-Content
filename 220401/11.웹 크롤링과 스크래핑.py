import requests
from bs4 import BeautifulSoup
url=("https://finance.naver.com/sise/sise_rise.naver")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

data1=soup.select("a.tltle")
data2=soup.select("td.number")



for j in range(0,999999999999,1):
    for i in data1[j]:
        print("종목명 :",i.text.strip(),end=",  ")
    for i in data2[j*10]:
        print("현재가 :",i.text.strip(),end=",  ")
    for i in data2[j*10+8]:
        print("PER :",i.text.strip())

