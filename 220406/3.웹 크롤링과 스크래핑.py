import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from bs4 import BeautifulSoup
b=webdriver.Chrome()
b.implicitly_wait(10)
b.get("https://www.naver.com")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a').click()
b.implicitly_wait(10)
b.find_element_by_xpath('/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[6]/a/span').click()
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="snb"]/ul/li[4]/a').click()
for i in range(1,6):
    #웹페이지동작
    print(f"{i}페이지")
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)") #제일 아래까지 휠 이동
    b.implicitly_wait(10)
    html = b.page_source
    b.implicitly_wait(10)
    b.find_element_by_xpath(f'//*[@id="main_content"]/div[3]/a[{i}]').click()
    #컴퓨터에서동작
    s = BeautifulSoup(html, "html.parser")
    data = s.select('dl')
    for i in data:
        if i.a:
            print(i.dd.previousSibling.previousSibling.a.text.strip())
            print(i.dd.span.text.strip())
    print("출력완료")

