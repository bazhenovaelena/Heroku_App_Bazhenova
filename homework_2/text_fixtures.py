import pytest

@pytest.fixture
def elements(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox_1 = checkboxes[0]
    checkbox_2 = checkboxes[1]
    return checkbox_1, checkbox_2