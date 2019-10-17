from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://sso.scut.edu.cn/cas/login")
elem = driver.find_element_by_id("un") #寻找账号输入框
elem.clear()
elem.send_keys("201764064356") #输入账号
password = driver.find_element_by_id('pd') #寻找密码输入框
password.clear()
password.send_keys("Raven991231") #输入密码
# input('输入验证码')
elem.send_keys(Keys.RETURN) #模拟键盘回车键
time.sleep(10)#这里可以直接sleep，也可以使用上一章讲到的等待某个条件出现
print(driver.page_source)
driver.quit()



