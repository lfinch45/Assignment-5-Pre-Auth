from common import Browser, Credentials, retry
from .locators import Locators


class CGS(Browser):
    def __init__(self, credentials: Credentials):
        super(CGS, self).__init__()
        self.credentials = credentials

    @retry()
    def login(self):
        self.browser.open_available_browser(self.credentials.url)
        self.browser.input_text_when_element_is_visible(Locators.username, self.credentials.username)
        self.browser.input_text_when_element_is_visible(Locators.password, self.credentials.password)
        self.browser.click_element_when_clickable(Locators.submit_button)