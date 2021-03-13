from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
# from openpyxl import Workbook
# from openpyxl import load_workbook
from os.path import expanduser
from os import path
import os
import csv
import urllib.request
# import xlsxwriter
# import xlrd
import string
# from openpyxl import load_workbook
from csv import writer 
import logging
import threading
import time
def data_scrap(url):
    driver.get(url)
    time.sleep(5)
    name1 = driver.find_element_by_xpath('/html/body/div[3]/section[1]/div[3]/div/div/h1').text
    name2 = driver.find_element_by_xpath('/html/body/div[3]/section[1]/div[3]/div/div/div[1]/span').text
    name = name1+' '+name2
    types = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/thead/tr/th[2]').text
    collection = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]').text.split(':')[1]
    finish = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[1]/div[3]/div/div').text.split(':')[1]
    grade = driver.find_element_by_xpath('/html/body/div[3]/section[1]/div[3]/div/div/div[4]').text.split(':')[1]
    color = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[1]/div[1]/div/div').text.split(':')[1]
    species = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[2]/div[1]').text.split(':')[1]
    Species_description = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[2]/div[2]/p').text
    grade_description = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[2]/div[4]/p').text

    availability = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]').text
    thickness = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
    RELATIVE_HUMIDITY = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
    MADE_IN = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[2]').text
    warranty = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[6]/td[2]').text
    INSTALLATION = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[7]/td[2]').text
    RADIANT_HEAT_APPROVED = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[9]/td[2]').text
    LEVEL = driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
    description = ""
    image = driver.find_element_by_xpath('/html/body/div[3]/section[1]/div[2]/img').get_attribute('src')
    List = [name, types, collection, finish, grade, color, species, Species_description, grade_description, availability, thickness, RELATIVE_HUMIDITY, MADE_IN, warranty, INSTALLATION, RADIANT_HEAT_APPROVED, LEVEL, description, image ]
    with open('sample.csv', 'a', encoding='utf-8-sig', newline='') as f_object: 
        writer_object = writer(f_object) 
        writer_object.writerow(List) 
        f_object.close() 
    time.sleep(5)

driver = webdriver.Chrome()
url = "https://appalachianflooring.com/product-category/flooring/?pa_type-de-construction=solid&lang=en"
driver.get(url)

while True:
    time.sleep(5)
    try:
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/nav/a').click()
    except:
        break
    # if no_more_lavel != True:
    #     load_more_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/nav/a')
    # if load_more_btn:
    #     load_more_btn.click()
    # else:
    #     no_more_lavel = True
    #     # no_more_lavel = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/nav/span')
    #     break

# li_count = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/p')
# count = li_count.text
# array = count.split(' ')
products = driver.find_element_by_class_name('products')
items = products.find_elements_by_tag_name('li')
product_url_list = []
for item in items:
    item_a_obj = item.find_element_by_class_name('woocommerce-LoopProduct-link')
    product_url_list.append(item_a_obj.get_attribute('href'))
for url in product_url_list:
    data_scrap(url)


