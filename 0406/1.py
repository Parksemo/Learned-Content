import warnings
warnings.filterwarnings('ignore')
import time
from selenium import webdriver
b=webdriver.Chrome() #컨트롤어 실행
b.implicitly_wait(10)#활성화 될때까지 대기
#time.slepp(초단위)스레드를 정지
b.get("http://www.naver.com")#요청 (페이지 이동)
b.implicitly_wait(10)
in_t=b.find_element_by_xpath('//*[@id="query"]')
in_t.send_keys("뉴스")
b.find_element_by_xpath('//*[@id="search_bth"]/span[2]').click()#마우스클릭
b.implicitly_wait(10)


