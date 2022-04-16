#동적 크롤링
import time
#import selenium #웹 자동화
from selenium import webdriver#웹 페이지 컨트롤러
from bs4 import BeautifulSoup
#op=webdriver.ChromeOptions()#웹 컨트롤러의 옵션틀 설정
#op.add_argument("window-size=1920x1080")#지정되 크기로 페이지 오픈
#봇으로 인식되지 않도록 설정을 한다.(단,직접적으로 페이지를 연다면 사용하지 않아도 된다.)
#op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
#b=webdriver.Chrome(options=op)#상위에 지정한 옵션으로 크롬 실행
#1.웹 자동화 장치 구축
b=webdriver.Chrome()
b.maximize_window()
#2.웹 자동화 장치실행(원하는 페이지까지 이동)
url="http://google.com"
b.get(url)
b.implicitly_wait(10)#활성화대기(웹 창 전부가 완성되었을때 동작 그리고 완성이 진행되지 않으면 예외 발생)
in_data=b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')#특정한 장소를 선택
in_data.send_keys("구글무비\n")#값입력
b.implicitly_wait(10)#활성화대기
link=b.find_element_by_xpath('//*[@id="tads"]/div/div/div/div/div[1]/a/div[1]/span')#링크 선택
link.click()#클릭 동작
b.implicitly_wait(10)#활성화대기
while True:#모든 내용 로드를 위한 동작
    info_n = b.execute_script("return document.body.scrollHeight")#로드된 내용의 최하단 크기확인
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")#로드된 내용의 최하단으로 이동
    # 확장
    time.sleep(2)
    next_n = b.execute_script("return document.body.scrollHeight")
    if info_n == next_n:  # 모든 내용을 담고있는 페이지 최하단
        break
html=b.page_source#3.페이지 크롤링
s=BeautifulSoup(html,'html.parser')#정렬도구(단수)
data=s.select('div.Epkrse')
for i in data:
    print(i.text)