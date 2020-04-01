from Selenium.automation_framework_prac.utilities import custom_logger_utility as cl
import logging
from Selenium.automation_framework_prac.base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _my_courses = 'My Courses'
    _all_courses = 'All Courses'
    _practice = 'Practice'
    _user_icon = "//li[@class='dropdown']"
    _edit_profile = "//a[contains(text(), 'Edit Profile')]"
    _manage_subscription = "//a[contains(text(), 'Manage Subscription')]"
    _change_credit_card = "//a[contains(text(), 'Add / Change Credit Card')]"
    _contact = "//a[contains(text(), 'Contact')]"
    _logout = "//a[contains(text(), 'Log Out')]"

    def navigateToMyCourses(self):
        self.elementClick(self._my_courses, 'linktext')

    def navigateToAllCourses(self):
        if self.isElementPresent(self._all_courses, 'linktext'):
            self.elementClick(self._all_courses, 'linktext')
        else:
            self.driver.get("https://learn.letskodeit.com/courses")

    def navigateToPractice(self):
        self.elementClick(self._practice, 'xpath')

    def navigateToUserIcon(self):
        self.elementClick(self._user_icon, 'xpath')

    def logOut(self):
        self.navigateToUserIcon()
        self.elementClick(self._logout, 'xpath')