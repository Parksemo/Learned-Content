from selenium import webdriver
from bs4 import BeautifulSoup
op=webdriver.ChromeOptions()
op.headless=True  #직접 창을 열지 않고 동작할때 사용
op.add_argument("window-size=1920x1080")
op.add_argument('user-agent=mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/100.0.4896.75 safari/537.36')
b=webdriver.Chrome(options=op)
b.maximize_window()
b.get("https://www.naver.com")
s=BeautifulSoup(b.page_source, 'html.parser')
print(s.text)
b.quit()