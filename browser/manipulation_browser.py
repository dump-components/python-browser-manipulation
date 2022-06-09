import time

from ..browser.browser import Browser

class ServiceManipulationBrowser(Browser):
    
    def __init__(self) -> None:
        super().__init__()
    
    def visit(self, url):
        self.dom.get(url)
        self.dom.maximize_window()
    
    def wait(self, timeout=10):
        self.dom.implicitly_wait(timeout)
    
    def find_element_by_xpath(self, xpath_element):
        element = self.dom.find_element_by_xpath(xpath_element)
        if element:
            return element
    
    def try_find_element_by_xpath(self, xpath_element, timeout=10):
        count = 0
        while count <= timeout:
            try:
                element = self.dom.find_element_by_xpath(xpath_element)
                time.sleep(1)
                return element
            except:
                count += 1
                time.sleep(1)
    
    def click_in_element_by_xpath(self, xpath_element):
        element = self.dom.find_element_by_xpath(xpath_element)
        if element:
            element.click()
            return True
        
    def send_text_in_element_by_xpath(self, xpath_element, input_text: str):
        element = self.dom.find_element_by_xpath(xpath_element)
        if element:
            element.send_keys(input_text)
            return True
        