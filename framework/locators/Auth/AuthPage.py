"""Локаторы по авторизации"""


class Auth:
    icon_profile = '//*[@data-test-id="menu-toggle-guest"]'
    button_auth = '//a[@class = "tm-user-menu__auth-button"]'
    login_form = "login_form"
    email_input = "email_field"
    password_input = "password_field"
    button_go = '//button[@name="go"]'
    auth_icon_profile = '//div[@data-test-id="menu-toggle-user"]'
    capcha = '//div[@class = "recaptcha-checkbox-border"]'
    my_tape = '//a[@class="tm-main-menu__item_active tm-main-menu__item"]'
    exit_auth = '//*[@rel="nofollow" and @class="tm-user-menu__menu-link tm-user-menu__menu-link_grey"]'
    user_name = '//*[@class="tm-user-item__username"]'
