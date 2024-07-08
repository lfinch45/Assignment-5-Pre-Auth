from common import Browser, Credentials, retry
from .locators import Locators


class TurningPoint(Browser):
    def __init__(self, credentials: Credentials):
        super(TurningPoint, self).__init__()
        self.credentials = credentials

    # SAMPLE FUNCTION, CHANGE IF NECESSARY
    @retry()
    def login(self):
        self.browser.open_available_browser(self.credentials.url)
        self.browser.input_text_when_element_is_visible(Locators.email, self.credentials.email)
        self.browser.input_text_when_element_is_visible(Locators.password, self.credentials.password)
        self.browser.click_element_when_clickable(Locators.login_button)