import allure
from selenium.webdriver.common.by import By

from framework.action.auth import authorization_user_habr
from framework.action.wait import wait_visible
from framework.locators.Auth.AuthPage import Auth


class TestLogin:

    @allure.story("Авторизация на сайте habr по e-mail")
    def test_login_account(self, driver):
        authorization_user_habr(driver)

        with allure.step('Проверяем что мы авторизовались под нашим пользователем'):
            tap_login_profile = driver.find_element_by_xpath(Auth().auth_icon_profile)
            tap_login_profile.click()
            wait_visible((By.XPATH, Auth().user_name))
            user_login = driver.find_element_by_xpath(Auth().user_name).text
            assert user_login == '@gW0eS', 'Нет логина пользователя или имя не совпало'

