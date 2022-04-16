import requests
from bs4 import BeautifulSoup
url=("https://finance.naver.com/sise/sise_rise.naver?sosok=1")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
data=soup.select("td")

def f(n,x):
    for i in range(x):
        n=n.next_sibling
    return n.text.strip()

for i in data:
    if i.a:
        print(f"종목명:{i.a.text},현재가:{f(i,2)},PER:{f(i,18)}")
