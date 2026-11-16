import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def elements(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox_1 = checkboxes[0]
    checkbox_2 = checkboxes[1]
    return checkbox_1, checkbox_2

@pytest.mark.basic
def test_checkbox_1_not_selected(browser, elements):
    checkbox_1 = elements[0]
    assert not checkbox_1.is_selected()


@pytest.mark.basic
def test_checkbox_1_is_selected(browser, elements):
    checkbox_1 = elements[0]
    checkbox_1.click()
    assert checkbox_1.is_selected()

@pytest.mark.basic
def test_checkbox_2_is_selected(browser, elements):
    checkbox_2 = elements[1]
    assert checkbox_2.is_selected()

@pytest.mark.basic
def test_checkbox_2_is_not_selected(browser, elements):
    checkbox_2 = elements[1]
    checkbox_2.click()
    assert not checkbox_2.is_selected()

