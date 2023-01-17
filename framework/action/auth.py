import allure
from selenium.webdriver.common.by import By

from framework.action.wait import wait_visible
from framework.locators.Auth.AuthPage import Auth


def authorization_user_habr(driver):
    login = 'ask.ev.dss@gmail.com'
    password = '* mGTdoMdCD4'

    with allure.step('Переходим на указанный сайт и переходим в профиль для авторизации'):
        driver.get('http://habr.com/')
        wait_visible((By.XPATH, Auth().icon_profile))
        tap_input_profile = driver.find_element(By.XPATH, Auth().icon_profile)
        tap_input_profile.click()
        wait_visible((By.XPATH, Auth().button_auth))
        tap_button_auth = driver.find_element(By.XPATH, Auth().button_auth)
        tap_button_auth.click()

    with allure.step('Переходим на указанный сайт и переходим в профиль для авторизации'):
        wait_visible((By.ID, Auth().login_form))
        email_input = driver.find_element(By.ID, Auth().email_input)
        email_input.send_keys(login)
        password_input = driver.find_element(By.ID, Auth().password_input)
        password_input.send_keys(password)
        tap_button_go = driver.find_element(By.XPATH, Auth().button_go)
        tap_button_go.click()
        wait_visible((By.XPATH, Auth().auth_icon_profile))
