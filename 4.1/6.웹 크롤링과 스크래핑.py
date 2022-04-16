import requests
from bs4 import BeautifulSoup
url=("http://www.hanbit.co.kr/store/books/full_book_list.html")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
data1=soup.find("li")
print(data1)
print('-'*20)
data2=data1.next_sibling.next_sibling
print(data2)
print('-'*20)
data3=data2.next_sibling.next_sibling
print(data3)
"""
print('-'*20)
data_all=soup.find_all("li")
print(data_all)
print('-'*20)

for i in data_all:
    print(i.get_text())
print('-'*20)
a=soup.find('a',text="한빛미디어")
print(a)
"""