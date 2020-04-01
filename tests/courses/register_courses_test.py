from Selenium.automation_framework_prac.utilities.teststatus import TestStatus
import pytest
import unittest
from Selenium.automation_framework_prac.pages.courses.register_course import RegisterCoursePage
from ddt import ddt, data, unpack


@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.rp = RegisterCoursePage(self.driver)

    @data(("", "Learn Python 3 from scratch"), ("JavaScript", "JavaScript for beginners",))
    @unpack
    def test_invalidCourseRegister(self, course_name, course_title,):
        self.rp.enroll_course(course_name, course_title=course_title)
        self.rp.register_course("5327532753275327", "1221", "223", "201301")
        result = self.rp.verifyErrorText("The card was declined")
        self.ts.markFinal("Invalid Course Registration", result, "Course register error Verification")
        self.driver.get("https://learn.letskodeit.com/courses")


