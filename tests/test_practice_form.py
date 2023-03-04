from selene import browser, be, have
import os


def test_practice_form(browser_settings):
    browser.element('#firstName').type('Dima')
    browser.element('#lastName').type('Nasedkin')
    browser.element('#userEmail').type('test@mail.com')
    browser.element('[for=gender-radio-1]').should(have.text('Male')).click()
    browser.element('#userNumber').type('89260010101')
    browser.element('#dateOfBirthInput').double_click().type('10').press_enter()
    browser.element('#subjectsInput').type('Accounting').press_enter()
    browser.element('[for=hobbies-checkbox-3]').should(have.text('Music')).click()
    #browser.element('#uploadPicture').should(have.text())
    browser.element('#uploadPicture').send_keys(pic)



#app > header > a > img
#state .css-1uccc91-singleValue