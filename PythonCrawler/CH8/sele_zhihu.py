from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.zhihu.com/#signin")
elem = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div/div[1]/div/form/div[2]/div/label/input") #寻找账号输入框
elem.clear()
elem.send_keys("13376585136") #输入账号
password = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div/form/div[3]/div/label/input') #寻找密码输入框
password.clear()
password.send_keys("Raven991124Zhihu") #输入密码
# input('请在网页上点击倒立的文字，完成以后回到这里按任意键继续。')
elem.send_keys(Keys.RETURN) #模拟键盘回车键
# time.sleep(10)#这里可以直接sleep，也可以使用上一章讲到的等待某个条件出现
# print(driver.page_source)
driver.quit()



