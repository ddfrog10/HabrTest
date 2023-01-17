import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent(browsers=['edge', 'chrome', 'firefox', 'google', 'safari'], fallback='chrome')
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
chrome_driver = WebDriver(chrome_options=options, executable_path=ChromeDriverManager().install())


@pytest.fixture
def driver(driver=chrome_driver):
    yield driver
    driver.save_screenshot('testResult.png')
    driver.close()
