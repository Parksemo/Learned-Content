import time
import csv
import requests
from bs4 import BeautifulSoup
url=("https://movie.naver.com/movie/point/af/list.naver?&page=")
#파일의 내용 정리
title="영화명","평점","리뷰"
f=open("save2.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
in_data=[]
#data수집
for page in range (1,3):
    print(f"page{page} 크롤링중")
    #1개의 페이지를 로드(스크래핑)
    r=requests.get(url+str(page))
    soup=BeautifulSoup(r.text,"html.parser")
    data=soup.find_all("td",attrs={"class":"title"})
    #파일 정리
    for i in data:
        if i.a:
            in_data.append([i.a.text, i.em.text, i.br.next_sibling.strip()])
            #단일 입력
            #in_data=[i.a.text,i.em.text,i.br.next_sibling.strip()]
            #writer.writerow(in_data)
    time.sleep(2)#빼먹으면 큰일난다!!!!!!!!
#저장
writer.writerow(in_data)


