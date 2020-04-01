import pytest
from Selenium.automation_framework_prac.base.webdriverfactory import WebDriverFactory
from Selenium.automation_framework_prac.pages.home.login_page import LoginPage


@pytest.yield_fixture()
def setUp():
    print("Running conftest method level setup")
    yield
    print("Running conftest method level teardown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running conftest one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", 'abcabc')

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("Running conftest one time teardown")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")