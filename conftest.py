from config import HOST
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    """command-line options"""
    parser.addoption('--host',
                     default=HOST,
                     action='store',
                     help='host fo testing')
    parser.addoption('--headless',
                     default=False,
                     action='store',
                     help='headless option for UI')


# Фикстура для получения host из командной строки
@pytest.fixture(scope='session')
def cmd_host(request):
    """Return data from cmd
    :request source_host
    :response: host
    """
    host = request.config.getoption('--host')
    return host


# Фикстура для получения browser из командной строки
@pytest.fixture(scope='session')
def cmd_browser(request):
    browser_from_cmd = request.config.getoption('--browser')
    if browser_from_cmd == 'chrome' or 'firefox':
        return browser_from_cmd
    else:
        raise ValueError(f'Для тестирования в {browser_from_cmd} не настроена конфигурация')


@pytest.fixture(scope='session')
def browser(cmd_browser, request):
    if cmd_browser == 'chrome':
        options = webdriver.ChromeOptions()
        if request.config.getoption('--headless'):
            options.add_argument("--headless=new")
        try:
            driver = webdriver.Chrome(options=options)
        except Exception:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        options = webdriver.FirefoxOptions()
        if request.config.getoption('--headless'):
            options.add_argument("--headless=new")
        try:
            driver = webdriver.Firefox()
        except Exception:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


