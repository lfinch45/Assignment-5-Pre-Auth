from common import Browser, Credentials, retry
from .locators import Locators


class Evicore(Browser):
    def __init__(self, credentials: Credentials):
        super(Evicore, self).__init__()
        self.credentials = credentials
        
    @retry()
    def login(self):
        self.browser.open_available_browser(self.credentials.url)
        self.browser.click_element_when_clickable(Locators.provider_button)
        self.browser.click_element_when_clickable(Locators.first_login_button)
        self.change_to_frame(Locators.iframe)
        self.browser.input_text_when_element_is_visible(Locators.user_id, self.credentials.customer_id)
        self.browser.input_text_when_element_is_visible(Locators.password, self.credentials.password)
        self.browser.click_element_when_clickable(Locators.agree_checkbox)
        self.browser.click_element_when_clickable(Locators.login_button)