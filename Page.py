from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

execfile("JsApiWrapper.py")


class GooglePage:
    search_locator = "lst-ib"

    def __init__(self, driver):
        self.driver = driver

    def search(self):
        search = self.driver.find_element_by_id(self.search_locator)
        return search

    def search_value(self):
        self.search().send_keys("Pink Floyd")

    def search_enter(self):
        self.search().send_keys(Keys.RETURN)