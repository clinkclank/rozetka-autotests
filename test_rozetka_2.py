import unittest
from selenium import webdriver

class LogInFB(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome("C:\\crossbrowser drivers\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://rozetka.com.ua/")

        # block notification
        self.block_notification = self.driver.find_element_by_css_selector("div.notificationPanelBlock")
        self.block_notification.click()

    def test_log_in(self):
        # get to the log in functionality
        self.log_in_link = self.driver.find_element_by_link_text("войдите в личный кабинет")

        # check log in functionality is present
        self.assertTrue(self.log_in_link.is_displayed())

        # click login link
        self.log_in_link.click()

        # get to the log in link from FB
        self.log_in_link_FB = self.driver.find_element_by_link_text("Facebook")

        # check log in from FB is displayed and enabled
        self.assertTrue(self.log_in_link_FB.is_displayed()
                        and self.log_in_link_FB.is_enabled())

        # click log in from FB link
        self.log_in_link_FB.click()

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()



