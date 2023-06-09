"""Методы OnlineMainPage"""
from config import HOST
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    ONLINE_BANKING = By.XPATH("//span[@text='ВТБ ОНЛАЙН']")

    def __init__(self, browser):
        super().__init__(browser)

    def submit_entrace_online(self):
        self.open(HOST).button_submit(locator=self.ONLINE_BANKING)




