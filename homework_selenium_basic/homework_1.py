from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable=notifications')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
add_element = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
add_element.click()
add_element.click()

delete_elements = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
assert len(delete_elements) == 2

delete_elements[0].click()
assert len(delete_elements) == 1

driver.quit()
