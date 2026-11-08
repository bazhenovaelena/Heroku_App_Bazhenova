import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_add_element(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = browser.find_element(By.XPATH, '//button[text()="Add Element"]')
    add_element.click()
    add_element.click()
    delete_elements = browser.find_elements(By.XPATH, '//button[text()="Delete"]')
    assert len(delete_elements) == 2


@pytest.mark.basic
def test_1_delete_elements(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = browser.find_element(By.XPATH, '//button[text()="Add Element"]')
    add_element.click()
    add_element.click()
    delete_elements = browser.find_elements(By.XPATH, '//button[text()="Delete"]')
    delete_elements[0].click()
    delete_elements = browser.find_elements(By.XPATH, '//button[text()="Delete"]')
    assert len(delete_elements) == 1