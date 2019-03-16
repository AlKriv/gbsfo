from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from page.start_page import StartPage


class TestGoogle2:

    def setup_method(self):
        self.driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_gbsfo(self):
        self.start_page = StartPage(self.driver)
        self.start_page.open_page("https://www.google.com").send_request("gbsfo")

    def teardown_method(self):
        self.driver.close()
