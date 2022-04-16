import sqlite3
import requests
from bs4 import BeautifulSoup
url=("https://finance.naver.com/sise/sise_rise.naver?sosok=1")
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

data1=soup.select("td")
db="data.db"
data=[]

def f(n,x):
    for i in range(x):
        n=n.next_sibling
    return n.text.strip()

for i in data1:
    if i.a:
        data.append({'종목명':i.a.text,'현재가':f(i,2),'전일비':f(i,4),
                     '등락률':f(i,6),'거래량':f(i,8),'매수호가':f(i,10),
                     '매도호가':f(i,12),'매수총잔량':f(i,14),'매도총잔량':f(i,16),
                     'PER':f(i,18),'ROE':f(i,20)})


def 저장(db,data):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
                CREATE TABLE data (
                    종목명 text,
                    현재가 text,
                    전일비 text,
                    등락률 text,
                    거래량 text,
                    매수호가 text,
                    매도호가 text,
                    매수총잔량 text,
                    매도 총잔량 text,
                    PER text,
                    ROE text
                )
            ''')
    c.executemany('INSERT INTO data VALUES (:종목명, :현재가, :전일비, :등락률, :거래량, '
                  ':매수호가, :매도호가, :매수총잔량, :매도총잔량, :PER, :ROE)', data)
    conn.commit()
    conn.close()

def 출력(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(i)

저장(db,data)
출력(db)
