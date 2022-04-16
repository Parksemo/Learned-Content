import requests
from bs4 import BeautifulSoup
url=("https://finance.naver.com/sise/sise_rise.naver")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

data=soup.select("a.tltle")
print(data)

for i in data:
    print(i.text)
