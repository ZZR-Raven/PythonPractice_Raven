import re
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
from scrapy.selector import Selector
import scrapy
import lxml
from tqdm import tqdm,trange
import time


class driver_crawler(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def driverget(self,url):
        self.driver.get(url)

    def driver_pause(self,*args):
        if len(args) == 0 :
            input('pause')
        else :
            for values in args:
                input(str(values)) 
 

url_lg = '''https://www.amazon.com/-/zh/ap/signin?openid.pape.
max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%
2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openi
d.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usf
lex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fs
pecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http
%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&
 '''

user_driver = driver_crawler()
user_driver.driverget(url_lg)  
        
ac_xpath = '//*[@id="ap_email"]'
ctn_xpath = '//*[@id="continue"]'
user_driver.driver.find_element_by_xpath(ac_xpath).send_keys('2258435737@qq.com')
user_driver.driver.find_element_by_xpath(ctn_xpath).click()

psw_xpath = '//*[@id="ap_password"]'
pswenter_xpath = '//*[@id="signInSubmit"]'
user_driver.driver.find_element_by_xpath(psw_xpath).send_keys('12345678')
user_driver.driver_pause()
user_driver.driver.find_element_by_xpath(pswenter_xpath).click()
user_driver.driver_pause()

pd_url = 'https://www.amazon.com/LunchBots-Small-Protein-Packer-Toddler/dp/B07983SV7B/ref=pd_rhf_ee_s_gcx-rhf_1_11?_encoding=UTF8&pd_rd_i=B07983SV7B&pd_rd_r=1d22b2dc-f0ec-4b5c-a68e-d5611394752f&pd_rd_w=bHcZu&pd_rd_wg=5s1tP&pf_rd_p=e4428c85-fd48-4538-856a-c8e08f1d4118&pf_rd_r=5R70DQQE7PW2XX4SQQ3G&psc=1&refRID=5R70DQQE7PW2XX4SQQ3G'
user_driver.driverget(pd_url) 
user_driver.driver_pause()

saler_xpath = '//*[@id="sellerProfileTriggerId"]'
user_driver.driver.find_element_by_xpath(saler_xpath).click()
user_driver.driver_pause()

email_xpath = '//*[@id="seller-contact-button"]/span/a'
user_driver.driver.find_element_by_xpath(email_xpath).click()
user_driver.driver_pause()
        