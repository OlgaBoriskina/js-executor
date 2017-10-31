from selenium import webdriver

import time
import unittest

execfile("JS.py")
execfile("JsApiWrapper.py")
execfile("ExistenceScroll.py")
execfile("Page.py")


class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.base_url = "https://www.google.ru/"
        self.driver.get(self.base_url)

    def test_js(self):
        api = JsApiWrapper(self.driver)
        scroll = ExistenceScroll(self.driver)
        page = GooglePage(self.driver)
        print(api.width())
        scroll.existence_scroll()
        page.search_value()
        api.delete_cursor()
        page.search_enter()
        while api.wait_page() != "complete":
            time.sleep(3)
        scroll.existence_scroll()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()