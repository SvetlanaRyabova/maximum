"""Методы BasePage"""
from config import HOST
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from loguru import logger


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = HOST

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
        try:
            print(locator)
            print(self.browser.find_element(By.XPATH, value=locator))
            return self.browser.find_element(By.XPATH, value=locator)
        except NoSuchElementException:
            logger.info(f"Элемент {locator} не найден на странице")

    def get_elements(self, locator):
        """
        Найти элементы
        :param locator
        :return: elements
        """
        try:
            return self.browser.find_elements(By.XPATH, value=locator)
        except NoSuchElementException:
            logger.info(f"Элемент {locator} не найден на странице")

    def set_value(self, locator, value):
        logger.info(f"Установить значение {value}")
        element = self.get_element(locator)
        element.send_keys(value)
        return self

    def button_submit(self, locator):
        logger.info(f"Нажать на кнопку {locator}")
        button = self.get_element(locator)
        button.click()
        return self

    def get_value(self, locator):
        logger.info(f"Получить текста элемента {locator}")
        element = self.get_element(locator)
        return element.text

    def check_exists_element(self, locator):
        logger.info(f"Проверить наличие элемента {locator}")
        try:
            self.browser.find_element(By.XPATH, value=locator)
            return True
        except NoSuchElementException:
            return False

    def ignore_banner(self, locator):
        logger.info(f"Закрыть всплывающее окно")
        if self.check_exists_element(locator):
            self.button_submit(locator)
        return self

    def element_is_visible(self, locator):
        logger.info(f"Проверить наличие элемента")
        assert self.check_exists_element(locator), f"Элемента {locator} нет на странице"

    def element_is_not_visible(self, locator):
        logger.info(f"Проверить отсутствие элемента")
        assert self.check_exists_element(locator) is False, f"Элемент {locator} есть на странице"

    def switch_to_window(self):
        logger.info("Перейти в загруженное окно")
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return self
