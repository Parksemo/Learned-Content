import requests
from bs4 import BeautifulSoup
url=("http://www.hanbit.co.kr/store/books/full_book_list.html")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
"""
t1=soup.find("a") #<a>/<a>1개만
print(t1)
print(type(t1))
l_t1=list(t1)
print(len(l_t1))
for i in t1:
    print(i)

print("-"*20)

t2=soup.find("div") #<div>/<div>1개만
print(t2)
print(type(t2))
l_t2=list(t2)
print(len(l_t2))
for i in t2:
    print(i)

print("-"*20)

print(soup.a.get_text())
print(t1.get_text())

print("-"*20)
"""

t2=soup.find("div") #<div>/<div>1개만
print(t2.get_text())
#print(t2)
#print(type(t2))
#print(t2.a.get_text())

print("-"*100)
t2=t2.next_sibling.next_sibling
print(t2.get_text())
print("-"*100)

t3=soup.find_all("div")
sub_t3=list(t3)[:2]
for i in sub_t3:
    print(i.get_text())
    print("-"*20)
#print(t3)
#l_t3=list(t3)
#print(len(l_t3))
#print(l_t3[0])  #t2=soup.find("div")와 동일
#print(type(l_t3[0]))
#print(l_t3[0].a.get_text())
#for i in t3:
#    print(i.a.get_text())

