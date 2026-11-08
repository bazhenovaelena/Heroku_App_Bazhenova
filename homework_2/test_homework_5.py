import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_paragraph_typo(browser):
    browser.get("https://the-internet.herokuapp.com/typos")
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    text = paragraphs[1].text
    expected_text = "Sometimes you'll see a typo, other times you won't."
    typo = []

    for i in range(10):
        browser.refresh()
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        text = paragraphs[1].text
        if text != expected_text:
            typo.append(text)
            break
        print(f"{i}:", typo)
