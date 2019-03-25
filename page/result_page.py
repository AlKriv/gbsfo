from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.base_page import BasePage


class ResultPage(BasePage):

    LIST_RESULT = (By.CSS_SELECTOR, "div.rc")
    TEXT_RESULT = (By.CSS_SELECTOR, "h3")
    LINK_RESULT = (By.CSS_SELECTOR, "a")
    _TOOLS = (By.XPATH, "//div[@role='navigation']/div/div/div/div[2]/a")
    _TIME_SEARCH = (By.XPATH, "//div[@role='navigation']/div[2]/div/div[3]")
    _TIME_ONE_HOUR = (By.XPATH, "//div[@role='navigation']/div[2]/div//ul[2]//li[2]/a")

    def find_text_result(self, text):
        result = []
        result = self.driver.find_elements(*self.LIST_RESULT)
        for i in range(0, len(result)):
            if result[i].find_element(*self.TEXT_RESULT).text == text:
                result[i].find_element(*self.LINK_RESULT).send_keys(Keys.LEFT_CONTROL, Keys.SHIFT, Keys.ENTER)
        """переключаемся на другую вкладку"""

    def tools_click(self):
        self.driver.find_element(*self._TOOLS).click()
        return self

    def time_click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(*self._TIME_SEARCH))
        element.click()
        return self

    def time_click_one_hour(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(*self._TIME_ONE_HOUR))
        element.click()
        return self

    def time_get_text(self):
        return self.driver.find_element(*self._TIME_ONE_HOUR).text
