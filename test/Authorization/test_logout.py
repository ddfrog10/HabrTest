import allure
from selenium.webdriver.common.by import By

from framework.action.auth import authorization_user_habr
from framework.action.wait import wait_visible
from framework.locators.Auth.AuthPage import Auth
from framework.locators.Profile.ProfilePage import ProfileScreen


class TestLogout:

    @allure.story("Логаут на сайте habr")
    def test_logout_account(self, driver):
        with allure.step('Выполняем авторизацию и переходим в настройки профиля'):
            authorization_user_habr(driver)
            tap_icon_profile = driver.find_element_by_xpath(Auth().auth_icon_profile)
            tap_icon_profile.click()
            wait_visible((By.XPATH, ProfileScreen().setting_profile))

        with allure.step('Выполняем выход из акаунта'):
            tap_exit_profile = driver.find_element_by_xpath(Auth().exit_auth)
            tap_exit_profile.click()

        with allure.step('Выполняем проверку что мы вышли из акаунта'):
            wait_visible((By.XPATH, Auth().icon_profile))
            tap_input_profile = driver.find_element(By.XPATH, Auth().icon_profile)
            tap_input_profile.click()
            wait_visible((By.XPATH, Auth().button_auth))
            check_login = driver.find_element_by_xpath(Auth().button_auth).text
            assert check_login == 'Войти', 'Нет кнопки или не произошел разлогин'

