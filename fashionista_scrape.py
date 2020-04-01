
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



# FASHIONISTA SCRAPE WITH MOUSE CLICK FUNCTION

chromedriver = "/Library/Application Support/Google/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('https://fashionista.com/news')
action = ActionChains(browser)


# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="m-card--image-element"]')))
except TimeoutException:
    print('Timed out waiting for page to load')
    # browser.quit()


# element_to_click = browser.find_element_by_class_name("m-component-footer--loader m-button")
# #Create the object for Action Chains & perform
# actions = ActionChains(browser)
# actions.click(element_to_click).perform()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# browser.implicitly_wait(20)





# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements(By.XPATH, '//h2[@class="m-ellipsis--text m-card--header-text"]')



# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')

button = browser.find_element(By.XPATH, '//button[@class="m-component-footer--loader m-button"]')
# button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dismiss')))
# browser.implicitly_wait(20)
action.click(button).perform()


