from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ResultPage(BasePage):

    LIST_RESULT = (By.XPATH, "//div[@id='search']//div[@class='g']")

    def find_text_result(self, text):
        results = self.driver.find_elements(*self.LIST_RESULT)

