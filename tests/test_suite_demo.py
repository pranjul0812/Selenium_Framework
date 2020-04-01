import unittest
# import all the test classes
from Selenium.automation_framework_prac.tests.home.login_tests import LoginTests
from Selenium.automation_framework_prac.tests.courses.register_courses_csv_data_test import RegisterCoursesCSVDataTest


# Get all the test from the test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTest)

# Create a testsuite combining all the test classes
smoke_test = unittest.TestSuite([tc1, tc2])

# Run Test Runner using testSuite
unittest.TextTestRunner(verbosity=2).run(smoke_test)
