import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture
def find_dropdown(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    all_options = select.options
    option_0 = all_options[0]
    option_1 = all_options[1]
    option_2 = all_options[2]
    return select, dropdown, all_options, option_0, option_1, option_2

@pytest.mark.basic
def test_check_len_all_options(browser,find_dropdown):
    select, dropdown, all_options, option_0, option_1, option_2 = find_dropdown
    dropdown.click()
    assert len(all_options) == 3

@pytest.mark.basic
def test_check_options_text(browser, find_dropdown):
    select, dropdown,all_options, option_0, option_1, option_2 = find_dropdown
    assert option_0.text == "Please select an option"
    assert option_1.text == "Option 1"
    assert option_2.text == "Option 2"

@pytest.mark.basic
def test_all_options_are_displayed(browser, find_dropdown):
    select, dropdown, all_options, option_0, option_1, option_2 = find_dropdown
    assert option_0.is_displayed()
    assert option_1.is_displayed()
    assert option_2.is_displayed()

@pytest.mark.basic
def test_option_0_is_selected(browser, find_dropdown):
    select, dropdown, all_options, option_0, option_1, option_2 = find_dropdown
    select.select_by_index(0)
    assert option_0.is_selected()

@pytest.mark.basic
def test_option_1_is_selected(browser, find_dropdown):
    select, dropdown, all_options, option_0, option_1, option_2 = find_dropdown
    select.select_by_index(1)
    assert option_1.is_selected()

@pytest.mark.basic
def test_option_2_is_selected(browser, find_dropdown):
    select, dropdown, all_options, option_0, option_1, option_2 = find_dropdown
    select.select_by_index(2)
    assert option_2.is_selected()


