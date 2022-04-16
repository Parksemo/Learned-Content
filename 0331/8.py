import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    html=추출('http://www.hanbit.co.kr/store/books/full_book_list.html')
    data=정규화(html)
    저장('data.db',data)
    출력('data.db')

def 추출(url):
    f=urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html=f.read().decode(encoding)
    return html

def 정규화(html):
    data = []
    for partial_html in re.findall(r'<td class="left"><a.*?</td>',html,re.DOTALL):
        url=re.search(r'<a href="(.*?)">',partial_html).group(1)
        url='http://www.hanbit.co.kr'+url
        title=re.sub(r'<.*?>','',partial_html)
        title=unescape(title)
        data.append({'url':url,'title':title})
    return data

def 저장(db_path, data):
    conn=sqlite3.connect(db_path)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
        CREATE TABLE data (
            title text,
            url text
        )
    ''')
    c.executemany('INSERT INTO data VALUES (:title, :url)',data)
    conn.commit()
    conn.close()


def 출력(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(i)


if __name__=="__main__":
    main()

