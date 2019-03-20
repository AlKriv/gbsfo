from selenium.webdriver.android.webdriver import WebDriver


class BasePage:
    driver: WebDriver = None

    def __init__(self, driver):
        self.driver = driver
