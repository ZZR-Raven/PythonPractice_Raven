from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
locator = (By.CLASS_NAME,'content')

try:
    WebDriverWait(driver,30).until(EC.presence_of_all_elements_located(locator))
    # WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.CLASS_NAME,'content'),'通关'))
    # driver.find_element_by_id('content')
except Exception as _:
    print('网页加载太慢，不想等了')
print(driver.page_source)

