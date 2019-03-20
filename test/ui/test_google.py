from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from page.start_page import StartPage
from page.result_page import ResultPage

class TestGoogle2:

    def setup_method(self):
        self.driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_gbsfo(self):

        StartPage(self.driver).\
            open_page("https://www.google.com").\
            send_request("gbsfo")
        ResultPage(self.driver).\
            find_text_result("gbsfo")

