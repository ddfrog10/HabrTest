import allure
from selenium.webdriver.common.by import By

from framework.action.auth import authorization_user_habr
from framework.action.wait import wait_visible
from framework.locators.Auth.AuthPage import Auth
from framework.locators.Profile.ProfilePage import ProfileScreen
from framework.locators.Main.favourites_page import FavouritesScreen
from framework.locators.Main.main_page import MainScreen


class TestFavourites:

    @allure.story("Добавление статьи в закладки.")
    def test_add_favourites(self, driver):
        with allure.step('Выполняем авторизацию и переходим на главную'):
            authorization_user_habr(driver)
            tap_main = driver.find_element_by_xpath(MainScreen().return_main)
            tap_main.click()

        with allure.step('Добавляем статью в избранное'):
            wait_visible((By.CSS_SELECTOR, MainScreen().section_name))
            tap_fov = driver.find_element_by_xpath(FavouritesScreen().add_favourites)
            tap_fov.click()

        with allure.step('Переходим в раздел с избранным'):
            wait_visible((By.XPATH, Auth().auth_icon_profile))
            tap_icon_profile = driver.find_element_by_xpath(Auth().auth_icon_profile)
            tap_icon_profile.click()
            wait_visible((By.XPATH, ProfileScreen().setting_profile))
            tap_my_fov = driver.find_element_by_xpath(FavouritesScreen().my_favourites)
            tap_my_fov.click()

        with allure.step('Проверяем наличие добавленной статьи в избранном'):
            wait_visible((By.XPATH, FavouritesScreen().list_favourites))
            tap_del_fov = driver.find_element_by_xpath(FavouritesScreen().delete_favourites)
            assert tap_del_fov.is_displayed(), 'В разделе нет добавленной закладки'

        with allure.step('Постусловие: Удаляем статью из избранного'):
            tap_del_fov.click()
