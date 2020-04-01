from selenium import webdriver
import os


class WebDriverFactory:

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://www.letskodeit.com/"

        if self.browser == "ie":
            driverLocation = "C:\\Pranjul\\webdriver\\ie.exe"
            os.environ['webdriver.driver.ie'] = driverLocation
            driver = webdriver.Ie(driverLocation)

        else:
            driverLocation = "C:\\Pranjul\\webdriver\\chromedriver.exe"
            os.environ['webdriver.driver.chrome'] = driverLocation
            driver = webdriver.Chrome(driverLocation)

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver

