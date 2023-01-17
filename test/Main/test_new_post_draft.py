import time

import allure
from selenium.webdriver.common.by import By

from framework.action.auth import authorization_user_habr
from framework.action.wait import wait_visible
from framework.locators.Main.main_page import MainScreen
from framework.locators.Main.post_page import PostScreen


class TestNewPost:

    @allure.story("Написание нового поста в черновик")
    def test_writing_new_post_draft(self, driver):
        title_text = 'Test'

        with allure.step('Выполняем авторизацию и переходим в раздел создания поста'):
            authorization_user_habr(driver)
            tap_edit_text = driver.find_element(By.XPATH, MainScreen().pencil_icon)
            tap_edit_text.click()
            wait_visible((By.XPATH, PostScreen().header_text))

        with allure.step('Заполняем пост и сохраняем черновик'):
            tap_write_title = driver.find_element_by_xpath(PostScreen().header_text)
            tap_write_title.send_keys(title_text)
            wait_visible((By.XPATH, PostScreen().save_text))
            tap_edit_text.click()

        with allure.step('Возвращаемся обратно в сохраненный черновик'):
            wait_visible((By.XPATH, PostScreen().header_text))
            tap_button_restore = driver.find_element_by_xpath(PostScreen().button_restore)
            wait_visible((By.XPATH, PostScreen().button_restore))
            tap_button_restore.click()
            time.sleep(4)
            alert = driver.switch_to.alert
            alert.accept()

        with allure.step('Проверяем что текст сохранился в черновике'):
            wait_visible((By.XPATH, PostScreen().header_text_full))
            title_text_post = driver.find_element_by_xpath(PostScreen().header_text_full).text
            assert title_text_post == title_text, f"Текст {title_text_post} не совпал с ранее введенным - {title_text}"
