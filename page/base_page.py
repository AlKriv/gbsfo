from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: WebDriver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
