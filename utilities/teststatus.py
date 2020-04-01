from Selenium.automation_framework_prac.base.selenium_driver import SeleniumDriver
from Selenium.automation_framework_prac.utilities import custom_logger_utility as cl
import logging


class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("###Verification Successful:: "+ resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("###Verification Failed:: " + resultMessage)
                    self.getScreenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("###Verification Failed:: " + resultMessage)
                self.getScreenShot(resultMessage)

        except:
            self.resultList.append("FAIL")
            self.log.error("###Exception Occured!!!")
            self.getScreenShot(resultMessage)

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        Needs to be called atleast once in a test case
        should be the final test status of the test case
        """
        self.setResult(result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + "###Test Failed")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "###Test Successful")
            self.resultList.clear()
            assert True == True