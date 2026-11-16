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

driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
checkbox_1 = checkboxes[0]
checkbox_2 = checkboxes[1]

assert not checkbox_1.is_selected()
checkbox_1.click()
assert checkbox_1.is_selected()

assert checkbox_2.is_selected()
checkbox_2.click()
assert not checkbox_2.is_selected()





