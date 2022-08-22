from selenium import webdriver
        
capabilities = {
    "browserName": "chrome",
    "browserVersion": "95.0",
    "selenoid:options": {
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="https://selenoid.fipo.com.br/:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get("http://www.google.com") 