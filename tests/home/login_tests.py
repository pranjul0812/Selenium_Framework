from Selenium.automation_framework_prac.pages.home.login_page import LoginPage
import unittest
import pytest
from Selenium.automation_framework_prac.utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        yield self.driver
        self.driver.back()
        self.driver.back()


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("pranjul0812@gmail.com", "25december")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Valid Login Verification")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login()
        result = self.lp.verifyLoginFail()
        self.ts.mark(result, "Invalid Login Verifation")


