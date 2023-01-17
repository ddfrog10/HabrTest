from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import chrome_driver


class BaseTest:

    def wait(self, by=By, timeout=5):
        WebDriverWait(chrome_driver, timeout).until(
            EC.presence_of_element_located(by)
        )
