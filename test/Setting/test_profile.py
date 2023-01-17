import allure
from selenium.webdriver.common.by import By

from framework.action.auth import authorization_user_habr
from framework.action.wait import wait_visible
from framework.locators.Auth.AuthPage import Auth
from framework.locators.Profile.ProfilePage import ProfileScreen
from selenium.webdriver.support.ui import Select


class TestProfile:

    @allure.story("Настройки профиля: смена всех полей")
    def test_edit_profile(self, driver):
        with allure.step('Выполняем авторизацию и переходим в Настройки профиля -> Профиль'):
            authorization_user_habr(driver)
            tap_icon_profile = driver.find_element_by_xpath(Auth().auth_icon_profile)
            tap_icon_profile.click()
            wait_visible((By.XPATH, ProfileScreen().setting_profile))
            tap_setting_profile = driver.find_element_by_xpath(ProfileScreen().setting_profile)
            tap_setting_profile.click()
            wait_visible((By.XPATH, ProfileScreen().profile))

        with allure.step('Редактируем имя в профиле и заполняем специальность'):
            wait_visible((By.CSS_SELECTOR, ProfileScreen().name_profile))
            tap_edit_fullname = driver.find_element_by_css_selector(ProfileScreen().name_profile)
            tap_edit_fullname.clear()
            tap_edit_fullname.send_keys('Denis')
            tap_edit_speciality = driver.find_element_by_css_selector(ProfileScreen().speciality_profile)
            tap_edit_speciality.clear()
            tap_edit_speciality.send_keys('Test')

        with allure.step('Редактируем пол'):
            tap_gender = driver.find_element_by_css_selector(ProfileScreen().gender_profile)
            tap_gender.click()
            select_gender = Select(tap_gender)
            select_gender.select_by_visible_text('Мужской')

        with allure.step('Редактируем дату рождения (день, месяц, год)'):
            tap_day = driver.find_element_by_css_selector(ProfileScreen().birthday_day)
            tap_day.click()
            select_day = Select(tap_day)
            select_day.select_by_index(1)
            tap_month = driver.find_element_by_css_selector(ProfileScreen().birthday_month)
            tap_month.click()
            select_moth = Select(tap_month)
            select_moth.select_by_value('2')
            tap_year = driver.find_element_by_css_selector(ProfileScreen().birthday_year)
            tap_year.click()
            select_year = Select(tap_year)
            select_year.select_by_visible_text('1991')

        with allure.step('Редактируем поля Страна, регион и город'):
            tap_country = driver.find_element_by_css_selector(ProfileScreen().location_country)
            tap_country.click()
            select_country = Select(tap_country)
            select_country.select_by_visible_text('Россия')
            tap_region = driver.find_element_by_css_selector(ProfileScreen().location_region)
            tap_region.click()
            select_region = Select(tap_region)
            select_region.select_by_index(2)
            tap_city = driver.find_element_by_css_selector(ProfileScreen().location_city)
            tap_city.click()
            select_city = Select(tap_city)
            select_city.select_by_value('447159')

        with allure.step('Добавляем контактный данный - Сайт и ссылку на него'):
            tap_add_contact_type = driver.find_element_by_xpath(ProfileScreen().button_contacts)
            tap_add_contact_type.click()
            wait_visible((By.CSS_SELECTOR, ProfileScreen().contact_type))
            tap_contact_type = driver.find_element_by_css_selector(ProfileScreen().contact_type)
            tap_contact_type.click()
            select_contact_type = Select(tap_contact_type)
            select_contact_type.select_by_visible_text('Сайт')
            tap_contact_value = driver.find_element_by_css_selector(ProfileScreen().contact_value)
            tap_contact_value.send_keys('https://www.google.com/')

        with allure.step('Добавляем данные о платежных инструментах'):
            tap_payment_ym = driver.find_element_by_css_selector(ProfileScreen().payment_ym)
            tap_payment_ym.send_keys('12345678901')
            tap_payment_pay_pal = driver.find_element_by_css_selector(ProfileScreen().payment_pay_pal)
            tap_payment_pay_pal.send_keys('1234567890')
            tap_payment_webmoney = driver.find_element_by_css_selector(ProfileScreen().payment_webmoney)
            tap_payment_webmoney.send_keys('123456789012')

        with allure.step('Сохраняем изменения в профиле'):
            tap_button_save = driver.find_element_by_xpath(ProfileScreen().save_button)
            tap_button_save.click()
            wait_visible((By.XPATH, ProfileScreen().toast_success))
