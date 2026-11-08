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

driver.get("https://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("abc")
actual_value = input_field.get_attribute("abc")
assert actual_value != "abc"

input_field.send_keys("1")
actual_value = input_field.get_attribute("1")
assert actual_value == "1"

input_field.send_keys(Keys.ARROW_UP)
actual_value = input_field.get_attribute("2")
assert actual_value == "2"

input_field.send_keys(Keys.ARROW_DOWN)
input_field.send_keys(Keys.ARROW_DOWN)
actual_value = input_field.get_attribute("0")
assert actual_value == "0"


