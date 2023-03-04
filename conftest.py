from selene import browser
import pytest


@pytest.fixture
def browser_settings():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()
    browser.config.timeout = 6.0
    pic = 'https://github.com/vgnstr8edge/qa_quru_python_4_5/blob/b8bd61f607b4375ae09d8ce7f94732de6e0d9871/picture'