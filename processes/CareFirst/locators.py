class Locators:
    username = '//*[@id="okta-signin-username"]'
    password = '//*[@id="okta-signin-password"]'
    remember_user_checkbox = "//input[@type='checkbox' and @id='input41']" # Doesn't work
    login_button = '//button[.//span[contains(text(), "Login")]]'
