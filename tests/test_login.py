from pages.base_page import BasePage
from pages.main_page import MainPage


def test_login(browser):
    page = MainPage(browser)
    page.open(page.url)
