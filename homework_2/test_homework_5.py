import pytest
from selenium.webdriver.common.by import By

EXPECTED_TEXT = "Sometimes you'll see a typo, other times you won't."


@pytest.mark.basic
def test_paragraph_typo(browser):
    browser.get("https://the-internet.herokuapp.com/typos")

    typo_found = False

    for _ in range(10):
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        text = paragraphs[1].text
        if text != EXPECTED_TEXT:
            typo_found = True
            break
        browser.refresh()

    assert typo_found == True

