from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.base_page import BasePage


class StartPage(BasePage):

    SEARCH_INPUT = (By.NAME, "q")

    def open_page(self, url):
        self.driver.get(url)
        return self

    def send_request(self, request):
        self.driver.find_element(* self.SEARCH_INPUT).send_keys(request, Keys.ENTER)


