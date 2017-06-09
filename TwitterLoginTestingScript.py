#=============================================================================================
#             Automated Testing Script Written In Selenium & Python3 By Ryan Kavanaugh
#                           For Testing Twitter Login Feature In Chrome
#=============================================================================================

# Import Selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


#===================================================================
#                   Twitter Login Script
#===================================================================

# Open Up Twitter

twitterurl = "https://twitter.com/TheRealTank"

twitterurldriver = webdriver.Chrome()

twitterurldriver.get(twitterurl)


# Input login information into appropriate areas

twittername = twitterurldriver.find_element_by_class_name('js-signin-email')

twittername.send_keys('timothytehstah@gmail.com')

twitterpass = twitterurldriver.find_element_by_name('session[password]')

twitterpass.send_keys('Test12345$')


# Click the login button

twitterurldriver.find_element_by_class_name('js-submit').click()


#===================================================================
#===================================================================
