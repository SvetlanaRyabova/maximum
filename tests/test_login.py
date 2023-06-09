

from locators.main_page_online_locators import MainPageOnlineLocators
from pages.main_page_online import MainPageOnline
import pytest


@pytest.mark.parametrize("login, password, error",
                         [
                             (pytest.param("test", "test", MainPageOnlineLocators.TEXT_PASSWORD_MUST_BE_VALID)),
                             (pytest.param("test", "100500", MainPageOnlineLocators.TEXT_ENTRY_IS_NOT_POSSIBLE)),
                             (pytest.param("test", "", MainPageOnlineLocators.TEXT_FILL_THE_FIELD)),
                             (pytest.param("", "100500", MainPageOnlineLocators.TEXT_FILL_THE_FIELD)),
                             (pytest.param("", "", MainPageOnlineLocators.TEXT_FILL_THE_FIELD)),

                         ])
def test_login(browser, login, password, error):
    """
    Авторизация по логину и паролю
    """
    page = MainPageOnline(browser)
    page.authorized_by_login(login=login, password=password).element_is_visible(error)


def test_become_client(browser):
    """
    Новый клиент
    """
    page = MainPageOnline(browser)
    page.become_new_client().element_is_visible(MainPageOnlineLocators.TEXT_GIVE_PHONE_NUMBER)

