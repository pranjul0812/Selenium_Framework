from Selenium.automation_framework_prac.utilities import custom_logger_utility as cl
import logging
from Selenium.automation_framework_prac.base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'
    _verify_login_pass = "//span[text()='pranjul']"
    _verify_login_fail = "//div[contains(text(), 'Invalid email or password')]"
    _remove_popup = "//svg[@role='img']"

    def clickLoginLink(self):
        if self.isElementPresent(self._login_link, 'linktext'):
            self.elementClick(self._login_link, 'linktext')
        elif self.isElementPresent(self._remove_popup, 'xpath'):
            self.elementClick(self._remove_popup, 'xpath')
            self.clickLoginLink()
        else:
            self.log.error("Quitting driver not able to login")
            self.driver.quit()

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, 'name')

    def login(self, username="", password=""):
        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._verify_login_pass, 'xpath')
        return result

    def verifyLoginFail(self):
        result = self.isElementPresent(self._verify_login_fail, 'xpath')
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode Its")

