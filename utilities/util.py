import time
from traceback import print_stack
from Selenium.automation_framework_prac.utilities import custom_logger_utility as cl
import logging


class Util:
    log = cl.custom_logger(logging.DEBUG)

    def sleep(self, sec, info=""):
        if info is not None:
            self.log.info("Wait:: " + str(sec) + "seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            print_stack()

    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual text from Application Web UI --> " + actualText)
        self.log.info("Expected text from Application Web UI --> " + expectedText)

        if expectedText.lower() in actualText.lower():
            self.log.info("###Verification Text Contains")
            return True
        else:
            self.log.info("###Verification Text does not Contain")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual text from Application Web UI --> " + actualText)
        self.log.info("Expected text from Application Web UI --> " + expectedText)

        if expectedText.lower() == actualText.lower():
            self.log.info("###Verification Text Match")
            return True
        else:
            self.log.info("###Verification Text does not Match")
            return False

