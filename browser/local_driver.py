import os, glob

from system.operation_system import OperationSystem
from exceptions.exception_events import Logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class LocalDriver:
    
    
    def __init__(self) -> None:
        self._log = Logger()
        self.__os = OperationSystem()
        self.__chrome_driver_path = self.__os.directory.webdriver.value
        os.environ["webdriver.chrome.driver"] = self.__chrome_driver_path
    
    def browser(self):
        return webdriver.Chrome(executable_path=self.__chrome_driver_path, options=self.__add_extensions())
    
    def __add_extensions(self):
        if OperationSystem().env.extensions.value == 'true':
            chrome_options = Options()
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
            try:
                files = glob.glob(self.__os.directory.extensions.value + '*')
                for f in files:
                    chrome_options.add_extension(f)
                return chrome_options
            except Exception as err:
                self._log.critical(err)
    
    