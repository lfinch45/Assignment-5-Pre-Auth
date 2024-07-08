class Locators:
    provider_button = '//*[@aria-label="Open Providers Menu"]'
    first_login_button = '//button[@class="menu-link menu-link--0 menu-link--parent"]'
    user_id = '//*[@id="txtUserEmail" and @name="UserEmail"]'
    iframe = '//*[@id="child-menu-756862ae-573e-4bfc-9c32-e4d04e9cf709"]/div/iframe'
    # <input class="lgnInpt txtfontstyle form-control" autocomplete="off" data-val="true" data-val-regex="Please enter a valid Email Address" data-val-regex-pattern="^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$" data-val-required="The UserEmail field is required." id="txtUserEmail" name="UserEmail" placeholder="User ID" type="text" value="">
    password = '//*[@id="txtPassWord"]'
    agree_checkbox = '//*[@id="agree"]'
    login_button = '//button[contains(text(), "LOGIN")]'