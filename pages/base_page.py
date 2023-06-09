"""Методы BasePage"""
from config import HOST
from selenium.webdriver.common.by import By


class BasePage:
    ONLINE_BANKING = By.XPATH("//span[@text='ВТБ ОНЛАЙН']")

    def __init__(self, browser):
        self.browser = browser

    def open(self, url: str):
        """
        Метод открывает страницу
        :param url: страница
        """
        url = url or self.url
        self.browser.get(url)
        return self

    def get_element(self, locator: str):
        """
        Найти элемент
        :param locator
        :return: element
        """
        return self.browser.find_element(value=locator)

    def get_elements(self, locator):
        """
        Найти элементы
        :param locator
        :return: elements
        """
        return self.browser.find_elements(value=locator)

    def set_value(self, locator, value):
        element = self.get_element(locator)
        element.send_keys(value)
        return self

    def button_submit(self, locator):
        button = self.get_element(locator)
        button.click()
        return self

    def get_value(self, locator):
        element = self.get_element(locator)
        return element.text


