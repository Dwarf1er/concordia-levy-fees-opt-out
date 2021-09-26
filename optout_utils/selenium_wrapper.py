import optout_url
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def click_by_xpath(driver: WebDriver, xpath: str):
    '''Simple wrapper for Selenium's click() function by providing the current WebDriver and the desired XPath'''
    driver.find_element_by_xpath(xpath).click()

def send_keys_by_xpath(driver: WebDriver, xpath: str, keys: str):
    '''Simple wrapper for Selenium's send_keys() function by providing the current WebDriver, the desired XPath and the desired content to provide to send_keys()'''
    driver.find_element_by_xpath(xpath).send_keys(keys)

def instantiate_webdriver(browser:str) -> WebDriver:
    '''Simple wrapper for the instantiation of a Selenium WebDriver, the browser can be selected from the supported list:
    - Chrome
    - Chromium
    - Firefox
    - Edge (chromium based)

    Internet Explorer and Opera are supported by the webdriver-manager package's developer but I personally would not recommend their use and decided not to include them

    This will return a WebDriver for the selected browser
    '''
    driver = None
    if (browser == "chrome"):
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif (browser == "chromium"):
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif (browser == "firefox"):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif (browser == "edge"):
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    
    driver.maximize_window()
    driver.get(optout_url.get_current_semeseter_url())
    return driver