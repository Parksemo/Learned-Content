import time
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from bs4 import BeautifulSoup
data1=[]
data2=[]
날짜=[]
data3=[]
종가=[]
data4=[]
고가=[]
저가=[]
시가=[]
in_data=[]

b=webdriver.Chrome()
b.get("https://naver.com")
time.sleep(1)
b.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[3]/a').click()
time.sleep(1)
b.find_element_by_xpath('//*[@id="stock_items"]').send_keys("삼성전자\n")
time.sleep(2)
b.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody/tr[1]/td[1]/a').click()
time.sleep(1)
b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
b.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a/span').click()
time.sleep(2)
b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
frame=b.find_element_by_xpath('//*[@id="content"]/div[2]/iframe[2]')
b.switch_to.frame(frame)
#리스트에 저장
for i in range(2,7):
    time.sleep(2)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    b.implicitly_wait(10)
    html = b.page_source
    b.implicitly_wait(10)
    if i ==2:
        b.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[{i}]/a').click()
        b.implicitly_wait(10)
    elif i !=2:
        b.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[{i+1}]/a').click()
        b.implicitly_wait(10)
    s=BeautifulSoup(html,'html.parser')
    b.implicitly_wait(10)
    data1 = s.find_all('td', attrs={"align": "center"})
    data2 = s.find_all('td', attrs={"class": "num"})

    for i in data1:
        날짜.append(i.span.text)
    for i in data2:
        data3.append(i.span.text.strip())

#현재가,전일대비,등락율 분리
for i in range(len(data3)//6):
    종가.append(data3[i*6])
    data4.append(data3[i*6+2])
    고가.append(data3[i*6+3])
    저가.append(data3[i*6+4])
for i in range(len(data4)):
    시가.append(data4[i].replace("\n\t\t\t\t",""))

#csv저장
in_data = list(zip(날짜,종가,시가,고가,저가))
in_data.reverse()
df = pd.DataFrame(in_data, columns=["날짜","종가","시가","고가","저가"])
df.to_excel('PHJ.xlsx', index=False)