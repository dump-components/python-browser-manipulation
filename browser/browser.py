from .remote_driver import RemoteDriver
from .local_driver import LocalDriver
from system.operation_system import OperationSystem

class Browser:
    
    def __init__(self) -> None:
        if OperationSystem().env.remote_browser.value == 'true':
            self.__driver = RemoteDriver().browser()
        else:
            self.__driver = LocalDriver().browser()
    
    @property
    def dom(self):
        return self.__driver
