#=============================================================================================
#             Automated Testing Script written in Selenium & Python3 By Ryan Kavanaugh
#          This script is to test the google search/page title features
#=============================================================================================

# Import the required selenium tools for this test
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Head over to the google home page
driver.get("http://www.google.com")

# Print out the the page title for our reference:
print('Here is the title of our first page: ' + driver.title + '\n')

# find the element for the google search box
inputElement = driver.find_element_by_name("q")

# type our search into the google search box
inputElement.send_keys("Geckos for sale!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # We now wait for the page to refresh and the title to display our search
    WebDriverWait(driver, 10).until(EC.title_contains("Geckos for sale!"))

    # You should see "Geckos for sale! - Google Search"
    print('Here is the title of our page after the search: ' + driver.title + '\n')

    if driver.title == 'Geckos for sale! - Google Search':
       print('The title matches our search and has passed our test.' + '\n')

finally:
    driver.quit()
    
