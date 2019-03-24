from page.start_page import StartPage
from page.result_page import ResultPage
from page.gbsfo_page import GbsfoPage
from test.ui.test_base import TestBase


class TestGoogle2(TestBase):

    def test_gbsfo(self):

        StartPage(self.driver).\
            open_page("https://www.google.com").\
            send_request("gbsfo")
        ResultPage(self.driver).\
            find_text_result("GBSFO")
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = GbsfoPage(self.driver).get_mail()
        assert (text == "sales@gbsfo.com")
