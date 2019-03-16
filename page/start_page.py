from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class StartPage:
    driver: WebDriver = None
    SEARCH_INPUT = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
        return self

    def send_request(self, request):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(request)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)

