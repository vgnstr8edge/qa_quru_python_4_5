from selene import browser, be, have
import pytest


def test_practice_form(browser_settings):
    browser.element('#firstName').should(be.blank).type('Dima')
    browser.element('#lastName').should(be.blank).type('Nasedkin')
    browser.element('#userEmail').should(be.blank).type('test@mail.com')
    browser.element('#genterWrapper div:nth-child(1) > label').click()
    browser.element('#userNumber').should(be.blank).type('89260010101')
    browser.element('#dateOfBirthInput').double_click().type('10').press_enter()
    browser.element('#subjectsInput').should(be.blank).type('Autotesting')




