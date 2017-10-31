from selenium import webdriver

execfile("JsApiWrapper.py")


class ExistenceScroll:
    def __init__(self, driver):
        self.driver = driver

    def existence_scroll(self):
        js_api_wrapper = JsApiWrapper(self.driver)
        if js_api_wrapper.high_scroll() < js_api_wrapper.high_window():
            print('scroll exists')
        else:
            print ('scroll not exists')