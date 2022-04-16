import time
from selenium import webdriver #웹 컨트롤러
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.google.com")
browser.implicitly_wait(10)
#n=browser.find_element_by_css_selector("input.gLFyf.gsfi").send_keys("python")
n=browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
n.send_keys("뉴스")
browser.implicitly_wait(10)
n.send_keys(Keys.ENTER)
browser.implicitly_wait(10)
browser.execute_script("window.scrollTo(0, 500);")#스크롤을 500번 내린다.
browser.implicitly_wait(10)
l=browser.find_element_by_xpath("//*[@id='rso']/div[2]/div/div/div[1]/div/a/h3")
l.click()
browser.implicitly_wait(10)
browser.execute_script(f"window.scrollTo(0, 500);")


