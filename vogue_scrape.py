from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



chromedriver = "/Library/Application Support/Google/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.vogue.com/fashion-shows/fall-2019-ready-to-wear')
actions = ActionChains(browser)



test = browser.find_element_by_link_text('A. Teodoro')
actions.click(test).perform()

# # Wait 20 seconds for page to load
# timeout = 20
# try:
#     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="carousel--image"]')))
# except TimeoutException:
#     print('Timed out waiting for page to load')
#     # browser.quit()


# next page
form = browser.find_element_by_id('bx-form-1087222-step-1')
print(form)

browser.find_element(By.XPATH, '//button[@class="bx-button"]').click()
# print(button)
# actions.click(button).perform()
# browser.find_element(By.XPATH, '//button[@class="bx-button"]').click().perform()



# slideshow = browser.find_element(By.XPATH, '//div[@class="gallery-marker--label"]').click().perform()

    

# #Create the object for Action Chains
# actions = ActionChains(browser)
# actions.click(link)
# # perform the operation on the element
# actions.perform()


