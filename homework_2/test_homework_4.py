import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

@pytest.mark.basic
def test_input_letters(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")
    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys("abc")
    input_value = input_field.get_attribute("value")
    assert input_value != "abc"

@pytest.mark.basic
def test_input_number(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")
    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1")
    input_field.send_keys(Keys.ENTER)
    input_value = input_field.get_attribute("value")
    assert input_value == "1"

@pytest.mark.basic
def test_arrow_up(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")
    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys("10")
    input_field.send_keys(Keys.ARROW_UP)
    input_value = input_field.get_attribute("value")
    assert input_value == "11"

@pytest.mark.basic
def test_arrow_down(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")
    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys("10")
    input_field.send_keys(Keys.ARROW_DOWN)
    input_value = input_field.get_attribute("value")
    assert input_value == "9"


