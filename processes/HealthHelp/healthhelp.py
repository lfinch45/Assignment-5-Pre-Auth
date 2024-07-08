from common import Browser, Credentials, retry
from .locators import Locators


class HealthHelp(Browser):
    def __init__(self, credentials: Credentials):
        super(HealthHelp, self).__init__()
        self.credentials = credentials

    @retry()
    def login(self):
        self.browser.open_available_browser(self.credentials.url)
        self.browser.input_text_when_element_is_visible(Locators.user_id, self.credentials.customer_id)
        self.browser.input_text_when_element_is_visible(Locators.password, self.credentials.password)
        self.browser.click_element_when_clickable(Locators.submit_button)