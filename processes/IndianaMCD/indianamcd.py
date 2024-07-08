from common import Browser, Credentials, retry
from .locators import Locators


class IndianaMCD(Browser):
    def __init__(self, credentials: Credentials):
        super(IndianaMCD, self).__init__()
        self.credentials = credentials

    # AS FAR AS I CAN GET
    @retry()
    def login(self):
        self.browser.open_available_browser(self.credentials.url)
        self.browser.input_text_when_element_is_visible(Locators.user_id, self.credentials.customer_id)
        self.browser.click_element_when_clickable(Locators.login_button)
        self.browser.input_text_when_element_is_visible(Locators.city_born, self.credentials.city_born)
        self.browser.click_element_when_clickable(Locators.select_private_computer)
        self.browser.click_element_when_clickable(Locators.continue_button)
        # self.browser.input_text_when_element_is_visible(Locators.password, self.credentials.password)
        # self.browser.click_element_when_clickable(Locators.login_button)