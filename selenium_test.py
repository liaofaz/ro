from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.title)
driver.find_element_by_css_selector("input#kw" and ".s_ipt").send_keys("我的世界")
driver.find_element_by_id("su").click()

time.sleep(3)
driver.close()
