import requests
from bs4 import BeautifulSoup
url=("http://www.hanbit.co.kr/store/books/full_book_list.html")
r=requests.get(url)
#print(r.text)
soup=BeautifulSoup(r.text,"lxml")
#print(soup)                    #soup은 필요한 데이터 찾을때 사용
#print(soup.title.get_text())
#print(soup.a)
#print(soup.a['href'])
#print(soup.find('a',attrs={"href":"/store/books/look.php?p_code=B9483006177"}).get_text())
#print(soup.find('a',attrs={"href":"/store/books/look.php?p_code=B5744853316"}).get_text())
#print(soup.find(attrs={"href":"/store/books/look.php?p_code=B5744853316"}))
#print(soup.find('td'))
# attrs는 속성에 대한 정보 값을 알고 싶을 때 사용한다.

k=soup.find('div',attrs={'class':"full_book_list_wrap"})
print(k)
print(type(soup))
print(type(k))

