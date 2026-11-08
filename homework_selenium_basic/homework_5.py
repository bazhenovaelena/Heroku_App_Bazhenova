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

driver.get("https://the-internet.herokuapp.com/typos")
paragraphs = driver.find_elements(By.TAG_NAME, "p")
text = paragraphs[1].text
expected_text = "Sometimes you'll see a typo, other times you won't."
typo = []

for i in range(10):
    driver.refresh()
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    text = paragraphs[1].text
    if text != expected_text:
        typo.append(text)
        break
print(f"{i}:", typo)