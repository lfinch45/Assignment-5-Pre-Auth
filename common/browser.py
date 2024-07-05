from abc import ABC
from RPA.Browser.Selenium import Selenium
from .browser_chrome_binary import chrome_binary



class Browser(ABC):

    def __init__(self):
        self.browser = Selenium(timeout=15, implicit_wait=15, page_load_timeout=15)
        self._original_open_available_browser = self.browser.open_available_browser
        self.browser.open_available_browser = self.custom_open_available_browser
        self.browser.set_download_directory("download")

    
    def custom_open_available_browser(self, url):
        browser_options = {"arguments": ["--incognito", "--no-sandbox", "--disable-dev-shm-usage", "--remote-debugging-pipe"], "capabilities": {"acceptInsecureCerts": True}}
        browser_options["binary_location"] = chrome_binary #Only for dev mode, deployed version will have chrome binary on dockerfile
        return self._original_open_available_browser(url, browser_selection='chrome', options=browser_options)
    

    def element_exists(self, locator) -> bool:
        try:
            self.browser.wait_until_element_is_visible(locator)
            no_records = self.browser.find_elements(locator)
            if len(no_records) > 0:
                return True
        except Exception as e:
            return False
        
    
    def element_was_clicked(self, locator) -> bool:
        if self.element_exists(locator):
            self.browser.click_element_when_clickable(locator)
            return True
        return False