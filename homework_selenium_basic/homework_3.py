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

driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown = driver.find_element(By.ID, "dropdown")
dropdown.click()
select = Select(dropdown)
all_options = select.options
assert len(all_options) == 3

option_0 = all_options[0]
option_1 = all_options[1]
option_2 = all_options[2]
assert option_0.text == "Please select an option"
assert option_1.text == "Option 1"
assert option_2.text == "Option 2"

assert option_0.is_displayed()
assert option_1.is_displayed()
assert option_2.is_displayed()

select.select_by_index(0)
assert option_0.is_selected()

select.select_by_index(1)
assert option_1.is_selected()

select.select_by_index(2)
assert option_2.is_selected()





