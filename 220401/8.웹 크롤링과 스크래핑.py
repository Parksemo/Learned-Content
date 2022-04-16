import requests
from bs4 import BeautifulSoup
url=("http://www.hanbit.co.kr/store/books/full_book_list.html")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")


data=soup.find_all("td",attrs={"class":"left"})
print(data)
for i in data:
    if i.a:
        print(i.get_text())

print('-'*20)

for i in soup.select('td[class=left]'):
    if i.a:
        print(i.get_text())

