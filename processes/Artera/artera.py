from common import Browser, Credentials, retry
from .locators import Locators


class Artera(Browser):
    def __init__(self, credentials: Credentials):
        super(Artera, self).__init__()
        self.credentials = credentials

    # AS FAR AS I CAN GET
    @retry()
    def login(self):
        self.browser.open_available_browser(self.credentials.url)
        self.browser.input_text_when_element_is_visible(Locators.email, self.credentials.email)
        self.browser.click_element_when_clickable(Locators.continue_button)
        # Not able to get past continue button right now, below is a guess
        self.browser.input_text_when_element_is_visible(Locators.password, self.credentials.password)
        self.browser.click_element_when_clickable(Locators.login_button) 