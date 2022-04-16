import sqlite3
import requests
from bs4 import BeautifulSoup
url=("https://movie.naver.com/movie/point/af/list.naver?&page=")
page=10
r=requests.get(url+str(page))
soup=BeautifulSoup(r.text,"html.parser")

data3=soup.find_all("tr")
db="data.db"
data=[]

for i in data3:
    if i.a:
        data.append({'번호':i.td.text,'영화명':i.a.text,'평점':i.em.text,
                     '감상평':i.br.next_sibling.text.strip()})

def 저장(db,data):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
                CREATE TABLE data (
                    번호 text,
                    영화명 text,
                    평점 text,
                    감상평 text
                )
            ''')
    c.executemany('INSERT INTO data VALUES (:번호, :영화명, :평점, :감상평)', data)
    conn.commit()
    conn.close()

def 출력(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(f"<번호>",i[0],"<영화명>",i[1],"<평점>",i[2],"<감상평>",i[3])

저장(db,data)
출력(db)
