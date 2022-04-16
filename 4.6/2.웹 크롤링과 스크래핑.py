import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
b=webdriver.Chrome()
b.implicitly_wait(10)#
b.get("https://www.google.co.kr")
b.implicitly_wait(10)
in_t=b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
in_t.send_keys("Python Tutor")
b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="learnPane"]/p[1]/a/b').click()
