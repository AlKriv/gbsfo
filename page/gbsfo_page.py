from selenium.webdriver.common.by import By

from page.base_page import BasePage


class GbsfoPage(BasePage):

    _MAIL = (By.CSS_SELECTOR, "a.item.item_mail")

    def get_mail(self):
        return self.driver.find_element(*self._MAIL).text
