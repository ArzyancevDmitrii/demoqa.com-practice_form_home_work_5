
import selene


def test_add_todos():
    selene.browser.config.hold_browser_open = True
    selene.browser.open('https://demoqa.com/automation-practice-form')
    selene.browser.element('#firstName').should(selene.be.blank).type('Dmitrii')
    selene.browser.element('#lastName').should(selene.be.blank).type('Ivanov')
    selene.browser.element('#userEmail').should(selene.be.blank).type('demopochta@gmail.com')
    selene.browser.element('[for="gender-radio-1"]').click()
    selene.browser.element('#userNumber').should(selene.be.blank).type('9011110101')
    selene.browser.element('#dateOfBirthInput').click()
    selene.browser.element('select[class="react-datepicker__month-select"] option[value="9"]').click()
    selene.browser.element('select[class="react-datepicker__year-select"] option[value="1992"]').click()
    selene.browser.element('div[class="react-datepicker__day react-datepicker__day--020"]').click()
    selene.browser.element('#subjectsInput').type('maths').press_enter()
    selene.browser.element('#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label').click()
    selene.browser.element('#state').click()
    selene.browser.element('#react-select-3-option-3').click()
    selene.browser.element('[id^=react-select][id*=option-2]').click()








