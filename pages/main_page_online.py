"""Методы MainPageOnline"""

from locators.main_page_online_locators import MainPageOnlineLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class MainPageOnline(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def authorized_by_login(self, login: any = "",
                            password: any = ""):
        """Авторизация через логин и пароль"""
        MainPage(self.browser)\
            .submit_entrace_online()\
            .switch_to_window().ignore_banner(MainPageOnlineLocators.BUTTON_BANNER_CERTIFICATE)\
            .switch_to_window().button_submit(locator=MainPageOnlineLocators.BUTTON_AUTH_LOGIN)\
            .set_value(locator=MainPageOnlineLocators.INPUT_LOGIN, value=login)\
            .set_value(locator=MainPageOnlineLocators.INPUT_PASSWORD, value=password)\
            .button_submit(locator=MainPageOnlineLocators.BUTTON_SUBMIT_AUTH)
        return self

    def become_new_client(self):
        """Авторизация через логин и пароль"""
        MainPage(self.browser)\
            .submit_entrace_online()\
            .switch_to_window().ignore_banner(MainPageOnlineLocators.BUTTON_BANNER_CERTIFICATE)\
            .switch_to_window().button_submit(locator=MainPageOnlineLocators.BUTTON_AUTH_LOGIN)\
            .button_submit(locator=MainPageOnlineLocators.BUTTON_BECOME_CLIENT)
        return self



