"""Методы MainPage"""
from time import sleep


from config import HOST
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from loguru import logger


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def submit_entrace_online(self):
        """Перейти на страницу личного кабинета"""
        logger.info("Открыть главную страницу")
        self.open(HOST).button_submit(locator=MainPageLocators.ONLINE_BANKING)
        logger.info("Проверить наличие текста Частным лицам")
        self.element_is_visible(locator=MainPageLocators.TEXT_PRIVATE_PERSON)
        return self









