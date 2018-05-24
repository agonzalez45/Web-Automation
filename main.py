import timeit
import time
from time import sleep
import sys
import requests
#import ConfigParser
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import front
import json
from pprint import pprint

json_data=open('data.txt')
data = json.load(json_data)


###########headless##############
#options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(r"/Users/adolfogonzalez1/Downloads/chromedriver", chrome_options=options)
#################################
driver = webdriver.Chrome(r"/Users/adolfogonzalez1/Downloads/chromedriver")

site = "###" ###enter your website to run 

driver.get(site)


##########BY img###########################
#driver.find_element_by_xpath("""//img[@src='//assets.supremenewyork.com/149909/vi/CVsY6ESWH2w.jpg']
#""").click()
class Person:
    def __init__(self, fName, email, pNum, address, city, zip, state, ccNum, month, year, cvv):
        self.fName = fName
        self.email = email
        self.pNum = pNum
        self.address = address
        self.city = city
        self.zip = zip
        self.state = state
        self.ccNum = ccNum
        self.month = month
        self.year = year
        self.cvv = cvv


class items:
    def __init__(self, sName, color, type):
        self.sName = sName
        self.color = color
        self.type = type



if __name__ == "__main__":
    Adolfo = Person("name", "email", "phone", "address", "city","zip","state","card","month","year","ccv")
    tee = items("item name", "Checker", "Accessories")

#for i in range (0, len (data['Profile'])):
 #   print (data['Profile'][0]['email'])

##### BY NAME!!!!!!!!!!!!!!!!###############
driver.find_element_by_xpath('//*[contains(text(), "name of item")]/../following-sibling::p/a[contains(text(), "color")]').click()

############# half a second#################
time.sleep(0.5)

sizeDropDown = Select(driver.find_element_by_id('s'))
sizeDropDown.select_by_visible_text('size') # change size of your item
time.sleep(0.5)

driver.find_element_by_name("commit").click()

time.sleep(0.5)

driver.find_element_by_xpath("""//*[@id="cart"]/a[2]""").click()
time.sleep(1)
driver.find_element_by_xpath("""//*[@id="order_billing_name"]""").send_keys(data['Profile'][0]['name'])

#//*[@id="order_billing_name"]
#driver.find_element_by_id('order_billing_name').send_keys('Adolfo Gonzalez')
#driver.find_element_by_id('order_billing_name').click().send_keys(Adolfo.fName)

driver.find_element_by_xpath("""//*[@id="order_email"]""").send_keys(data['Profile'][0]['email'])

driver.find_element_by_xpath("""//*[@id="order_tel"]""").send_keys(data['Profile'][0]['phone'])

driver.find_element_by_xpath("""//*[@id="order_billing_zip"]""").send_keys(data['Profile'][0]['zip'])

driver.find_element_by_xpath("""//*[@id="bo"]""").send_keys(data['Profile'][0]['address'])

driver.find_element_by_xpath("""//*[@id="order_billing_city"]""").send_keys(data['Profile'][0]['city'])

driver.find_element_by_xpath("""//*[@id="nnaerb"]""").send_keys(data['Profile'][0]['credit card'])

driver.find_element_by_xpath("""//*[@id="credit_card_month"]""").send_keys(data['Profile'][0]['month'])

driver.find_element_by_xpath("""//*[@id="credit_card_year"]""").send_keys(data['Profile'][0]['year'])

driver.find_element_by_xpath("""//*[@id="orcer"]""").send_keys(data['Profile'][0]['cvv'])

driver.find_element_by_xpath("""//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins""").click()

time.sleep(0.5)





