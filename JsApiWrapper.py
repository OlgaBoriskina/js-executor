from selenium import webdriver

execfile("JS.py")


class JsApiWrapper:
    def __init__(self, driver):
        self.driver = driver

    def width(self):
        width_search = self.driver.execute_script(JS.width())
        return width_search

    def high_scroll(self):
        high_scroll = self.driver.execute_script(JS.high_scroll())
        return high_scroll

    def high_window(self):
        high_window = self.driver.execute_script(JS.high())
        return high_window

    def delete_cursor(self):
        delete_cursor = self.driver.execute_script(JS.delete_cursor())
        return delete_cursor

    def wait_page(self):
        wait_page = self.driver.execute_script(JS.wait_page())
        return wait_page