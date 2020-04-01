from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

 
# BUSINESS OF FASHION SCRAPE INCOGNITO WITH MOUSE FUNCTION




# FASHIONSNOOP SCRAPE WITH KEY & MOUSE FUNCTION

chromedriver = "/Library/Application Support/Google/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('https://fashionsnoops.com')
# action = ActionChains(browser)

# login to site

element_to_click = browser.find_element_by_class_name("signinclick")
#Create the object for Action Chains
actions = ActionChains(browser)
actions.click(element_to_click)
# perform the operation on the element
actions.perform()

username = browser.find_element(By.XPATH, '//input[@id="ctl00_txtUserName"]').send_keys("pearj567@newschool.edu")
# actions = ActionChains(browser)
actions.send_keys(Keys.TAB).perform()
password = browser.find_element(By.XPATH, '//input[@id="ctl00_txtPasswod"]').send_keys("fsssfw2019")
# actions.send_keys(login, 'pearj567@newschool.edu')
actions.perform()


element_to_click = browser.find_element_by_id("ctl00_btnLogin")
#Create the object for Action Chains & perform
actions = ActionChains(browser)
actions.click(element_to_click).perform()


# Wait 20 seconds for page to load
timeout = 30
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'NWH-top-img-block NH-top-img-block notshowfullbgstrech"')))
except TimeoutException:
    print('Timed out waiting for page to load')
    # browser.quit()

# # find_elements_by_xpath returns an array of selenium objects.
# titles_element = browser.find_elements(By.XPATH, '//h2[@class="m-ellipsis--text m-card--header-text"]')


# # use list comprehension to get the actual repo titles and not the selenium objects.
# titles = [x.text for x in titles_element]
# # print out all the titles.
# print('titles:')
# print(titles, '\n')

# # Click See More for addition posts
# results = browser.find_element_by_tag_name('button').click()
# print('results')
  




# FASHIONISTA SCRAPE WITH MOUSE CLICK FUNCTION

# chromedriver = "/Library/Application Support/Google/chromedriver"
# browser = webdriver.Chrome(chromedriver)
# browser.get('https://fashionista.com/news')
# action = ActionChains(browser)


# Wait 20 seconds for page to load
# timeout = 20
# try:
#     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'class="m-card--image-element"')))
# except TimeoutException:
#     print('Timed out waiting for page to load')
#     # browser.quit()


# # find_elements_by_xpath returns an array of selenium objects.
# titles_element = browser.find_elements(By.XPATH, '//h2[@class="m-ellipsis--text m-card--header-text"]')


# # use list comprehension to get the actual repo titles and not the selenium objects.
# titles = [x.text for x in titles_element]
# # print out all the titles.
# print('titles:')
# print(titles, '\n')

# # Click See More for addition posts
# results = browser.find_element_by_tag_name('button').click()
# print('results')
  