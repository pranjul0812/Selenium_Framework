from traceback import print_stack
from Selenium.automation_framework_prac.base.selenium_driver import SeleniumDriver
from Selenium.automation_framework_prac.utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

