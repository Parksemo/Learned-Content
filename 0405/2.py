import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
url=("https://news.naver.com/main/list.naver?mode=LS2D&sid2=228&sid1=105&mid=shm&date=20220404&page=")
r = requests.get(url + str(1),headers=headers)
r.raise_for_status()
htm1=r.text
s=BeautifulSoup(htm1,"html.parser")

data=s.select("dl")
for i in data:
    if i.a:
        print(i.dd.previous_sibling.previous_sibling.text.strip())

