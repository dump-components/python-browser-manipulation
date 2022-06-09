from system.operation_system import OperationSystem
from selenium import webdriver

class RemoteDriver:
    
    def __init__(self) -> None:
        self.__os = OperationSystem()
        
    def browser(self):
        host = self.__os.env.selenoid_host.value
        return webdriver.Remote(command_executor=host, desired_capabilities=self.__add_capabilities())
    
    def __add_capabilities(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--browserName=chrome')
        options.add_argument('--browser_version=95.0')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("start-maximized")
        options.add_argument("--disable-application-cache")
        capabilities = options.to_capabilities()
        capabilities["enableVNC"] = True
        return capabilities
