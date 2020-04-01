from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from traceback import print_stack
from selenium.common.exceptions import *
from Selenium.automation_framework_prac.utilities import custom_logger_utility as cl
import logging
from datetime import datetime
import os
from selenium.webdriver.common.keys import Keys


class SeleniumDriver:

    log = cl.custom_logger(logging.DEBUG)
    now = datetime.now()

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
       return self.driver.title

    def getScreenShot(self, resultMessage):
        fileName = resultMessage + "_" + self.now.strftime("%d%m%y_%H%M%S") + ".png"
        screenShotDirectory = "../screenshots/"
        relativeFileName = screenShotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: "+ destinationFile)
        except:
            self.log.error("###Exception Occured")
            print_stack()

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        else:
            self.log.info("locator type {0} is not correct/supported".format(locatorType))
        return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator as {0} and locator type as {1}".format(locator, locatorType))
        except:
            self.log.info("Element not found with locator as {0} and locator type as {1}".format(locator, locatorType))
        return element

    def getElementList(self, locator, locatorType='id'):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Elements found with locator as {0} and locator type as {1}".format(locator, locatorType))
        except:
            self.log.info("Elements not found with locator as {0} and locator type as {1}".format(locator, locatorType))
        return element

    def elementClick(self, locator="", locatorType= 'id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the element with locator as {0} and locator type as {1}".format(locator, locatorType))
        except:
            self.log.info("can't click on the element with locator as {0} and locator type as {1}".format(locator, locatorType))
            print_stack()

    def sendKeys(self, data, locator="", locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("send data:: {0} :: to the element with locator as {1} and locator type as {2}"
                  .format(data, locator, locatorType))
        except:
            self.log.info("can't send data:: {0} :: to the element with locator as {1} and locator type as {2}"
                  .format(data, locator, locatorType))
            print_stack()

    def searchData(self, data, locator="", locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            element.send_keys(Keys.ENTER)
            self.log.info("search data:: {0} :: to the element with locator as {1} and locator type as {2}"
                  .format(data, locator, locatorType))
        except:
            self.log.info("can't search data:: {0} :: to the element with locator as {1} and locator type as {2}"
                  .format(data, locator, locatorType))
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            self.log.debug("Before Finding Text")
            text = element.text
            self.log.debug("After Finding Text, size is:" + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text)!=0:
                self.log.info("Getting text on element::" + info)
                self.log.info("The Text is::'" + text + "'")
                text = text.strip()
        except:
            self.info.error("Failed to text on the element:: " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator as {0} and locator type as {1}".format(locator, locatorType))
                return True
            else:
                self.log.info("Element not present with locator as {0} and locator type as {1}".format(locator, locatorType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            isDisplayed = element.is_displayed()
            if isDisplayed:
                self.log.info("Element is displayed")
                return True
            else:
                self.log.info("Element is not displayed")
                return False
        except:
            self.log.error("Element not found")
            return False

    def waitForElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum:: {0} :: seconds for element to be clickable".format(timeout))
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the webpage")

        except:
            self.log.info("Element not appeared on the webpage")
            print_stack()
        return element

    def scroll(self, direction="up", value="1000"):
        if direction.lower() == "up":
            self.driver.execute_script("window.scrollBy(0, -(arguments[0]))", value)
            self.log.info("Scrolled the Webpage upwards")
        else:
            self.driver.execute_script("window.scrollBy(0, (arguments[0]))", value)
            self.log.info("Scrolled the Webpage downwards")

    def scrollToElement(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            self.driver.execute_script("arguments[0].scrollIntoView(true)", element)
            self.log.info("Scrolled to :: " + info)
        except:
            self.log.error("Failed to scrolled to ::" + info)
            print_stack()

    def getCurrentHandle(self):
        handle = self.driver.current_window_handle
        self.log.info("Current Handle is: " + str(handle))
        return handle

    def switchToWindow(self, handle):
        self.driver.switch_to.window(handle)
        self.log.info("Switched to Handle:: " + handle)

    def switchToFrame(self, value):
        self.driver.switch_to.frame(value)
        self.log.info("Switch to Iframe :: " + str(value))

    def dataFillingForMutipleIframes(self, value, data, locator, locatorType, parentHandle):
        self.switchToFrame(value)
        self.sendKeys(data, locator, locatorType)
        self.switchToWindow(parentHandle)







