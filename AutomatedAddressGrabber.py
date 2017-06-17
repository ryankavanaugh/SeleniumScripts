import xlrd
import xlwt
import requests
from bs4 import BeautifulSoup as Soup
import urllib.request
from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# EXCEL WORKBOOK
    # open up the workbook
workbook = xlrd.open_workbook('JSList01.xlsx')
    # open up the worksheet
worksheet = workbook.sheet_by_name('Sheet1')

#workbook2 = xlwt

print('\n')

#=================================================
# THE LOOP
for current_row in range(worksheet.nrows):
    # ================================================
    # CHROME DRIVER
    driver = webdriver.Chrome()
    driver.get('http://www.google.com')
    # element for the google search box
    inputElement = driver.find_element_by_name("q")

    # =================================================

    fname_text = worksheet.row(current_row)[0]

    inputElement.send_keys(fname_text.value)
    inputElement.submit()

    WebDriverWait(driver, 10).until(EC.title_contains(fname_text.value))
    print(fname_text.value)

    try:
        element = driver.find_element_by_xpath("//*[@id='rhs_block']/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]")
        print(element.text)
    except:
        print("Retrieve Address Manually")
        pass

  #  worksheet.write(current_row, 1, element.text)
    print('\n')
    #driver.get('http://www.google.com')
    #THIS PART NEEDS TO OPEN THE BROWSER AND GRAB THE ADDRESS OF EACH PLACE

    #1 ACCESS THE BROWSER

    #2 TYPE


    #lname_text = worksheet.row(current_row)[1]
    #age = worksheet.row(current_row)[2]
    #print(fname_text, lname_text, age)


    driver.quit()