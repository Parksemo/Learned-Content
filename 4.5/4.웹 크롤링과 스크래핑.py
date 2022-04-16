from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
id="" #로그인할 id
pw="" #로그인할 pw
b=webdriver.Chrome()
b.implicitly_wait(10)
b.get("http://naver.com")
b.implicitly_wait(10)
lc=b.find_element_by_class_name('link_login')
lc.click()
b.implicitly_wait(10)
#id 입력
in_id=b.find_element_by_id('id')
in_id.click()
pyperclip.copy(id) #복사
in_id.send_keys(Keys.CONTROL,'v')#붙여넣기
b.implicitly_wait(10)
#pw 입력
in_pw=b.find_element_by_id('pw')
in_pw.click()
pyperclip.copy(pw)#복사
in_pw.send_keys(Keys.CONTROL,'v')#붙여넣기
b.implicitly_wait(10)
b.find_element_by_id('log.login').click()
b.implicitly_wait(10)
ns=b.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a')
ns.click()
b.implicitly_wait(10)
ns_it=b.find_element_by_xpath('/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[6]/a/span')
ns_it.click()
b.implicitly_wait(10)
ns_it_it=b.find_element_by_xpath('//*[@id="snb"]/ul/li[4]/a')
ns_it_it.click()
b.implicitly_wait(10)
data_l=[]
for i in range(1,11):
    data_l.append(b.find_element_by_xpath(f'//*[@id="main_content"]/div[2]/ul[1]/li[{i}]/dl/dt[2]/a').text)
    b.implicitly_wait(10)
print(data_l)

