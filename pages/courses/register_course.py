from Selenium.automation_framework_prac.utilities import custom_logger_utility as cl
from Selenium.automation_framework_prac.base.basepage import BasePage
import logging
from Selenium.automation_framework_prac.utilities.util import Util
import time


class RegisterCoursePage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    _allCourses = "All Courses"
    _courseSearchBar = "search-courses"  # id
    _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
    _enrollButton = "enroll-button-top"  # id
    _paymentMethod = "//button[@class = 'dropbtn minimal']"
    _cardNum = "//input[@name = 'cardnumber']"
    _expirationDate = "//input[@name = 'exp-date']"
    _cvv = "//input[@name = 'cvc']"
    _postal = "//input[@name = 'postal']"
    _billingLocation = "//input[@value='IN']"
    _termNPrivacyBox = "agreed_to_terms_checkbox"  # id
    _purchaseButton = "confirm-purchase"  # id
    _paymentError = '//div[@class="payment-error-box"]//span[contains(text(), "The card was declined")]'

    def all_courses(self):
        self.elementClick(self._allCourses, 'linktext')

    def search_course(self, course_name):
        self.searchData(course_name, self._courseSearchBar)

    def find_course(self, course_title):
        if self.isElementPresent(self._course.format(course_title), 'xpath'):
            self.log.info(course_title + " is available")
            return True
        else:
            self.log.error("No Course for :: " + course_title)
            return False

    def select_course(self, course_title):
        self.log.info("Selecting the course :: " + course_title)
        self.elementClick(self._course.format(course_title), 'xpath')

    def enroll_course(self, course_name="", course_title='JavaScript For Beginners'):
        if course_name:
            self.search_course(course_name)
        else:
            self.all_courses()
        if self.find_course(course_title):
            self.select_course(course_title)
            self.elementClick(self._enrollButton)
        else:
            self.log.error("Can't register course :: " + course_title)

    def cardDetailsEntry(self, frame_value, data, locator, locatorType, parentHandle):
        self.switchToFrame(frame_value)
        element = self.getElement(locator, locatorType)
        elementarray = [char for char in data]
        for char in elementarray:
            self.sendKeys(char, element=element)
        self.switchToWindow(parentHandle)

    def enter_card_details(self, cardNumber, expDate, cvv, zip):
        self.scrollToElement(self._paymentMethod, 'xpath', info="Payment Method")
        parentHandle = self.getCurrentHandle()
        self.cardDetailsEntry("__privateStripeFrame8", cardNumber, self._cardNum, 'xpath', parentHandle)
        self.cardDetailsEntry("__privateStripeFrame9", expDate, self._expirationDate, 'xpath', parentHandle)
        self.cardDetailsEntry("__privateStripeFrame10", cvv, self._cvv, 'xpath', parentHandle)
        self.cardDetailsEntry("__privateStripeFrame11", zip, self._postal, 'xpath', parentHandle)

    def selectBillingLocation(self):
        if self.isElementPresent(self._billingLocation, 'xpath'):
            self.elementClick(self._billingLocation, 'xpath')
        self.elementClick(self._termNPrivacyBox)
        time.sleep(2)

    def purchase_course(self):
        self.elementClick(self._purchaseButton)

    def register_course(self, cardNumber, expDate, cvv, zip):
            self.enter_card_details(cardNumber, expDate, cvv, zip)
            self.selectBillingLocation()
            self.purchase_course()

    def verifyRegisterCourseFail(self):
        failElement = self.waitForElement(self._paymentError, "xpath")
        if self.isElementDisplayed(element=failElement):
            result = True
        else:
            result = False
        return result

    def verifyErrorText(self, expected_error):
        if self.verifyRegisterCourseFail():
            text = self.getText(self._paymentError, locatorType='xpath', info="Payment Error")
            self.log.info("Payment Error :" + text)
            result = self.util.verifyTextContains(text, expected_error)
        else:
            result = False
        return result











