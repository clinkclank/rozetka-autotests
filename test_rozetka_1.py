import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
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

    def test_search_by_category(self):
        # get the search text input field
        self.search_field = self.driver.find_element_by_xpath("//input[@name='text']")

        # enter search keyword
        self.search_field.send_keys("Asus")

        # select the category Компьютеры и ноутбуки
        self.search_category = self.driver.find_element_by_name("rz-search-category-value")
        self.search_category.click()
        self.category_computers = self.driver.find_element_by_link_text("Компьютеры и ноутбуки")
        self.category_computers.click()

        # seach by selecting parameters
        self.search_button = self.driver.find_element_by_name("rz-search-button")
        self.search_button.click()
        self.search_results = self.driver.find_elements_by_xpath("//div[@data-location='searchResults']");
        self.assertGreaterEqual(len(self.search_results), 1, 'should be more than 1 result');

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()





