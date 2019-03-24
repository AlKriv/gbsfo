from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.base_page import BasePage


class ResultPage(BasePage):

    LIST_RESULT = (By.CSS_SELECTOR, "div.rc")
    TEXT_RESULT = (By.CSS_SELECTOR, "h3")
    LINK_RESULT = (By.CSS_SELECTOR, "a")

    def find_text_result(self, text):
        result = []
        result = self.driver.find_elements(*self.LIST_RESULT)
        for i in range(0, len(result)):
            if result[i].find_element(*self.TEXT_RESULT).text == text:
                result[i].find_element(*self.LINK_RESULT).send_keys(Keys.LEFT_CONTROL, Keys.SHIFT, Keys.ENTER)
        """переключаемся на другую вкладку"""

