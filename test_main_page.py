from .pages.main_page import MainPage
from .pages.main_page import LoginPage
import pytest

link1 = "https://planoplan.com/"


def test_changing_the_language_button_main_page(browser):
    page = MainPage(browser, link1)
    page.open()
    page.changing_the_language_button_main_page()


def test_logo_click_main_page(browser):
    page = MainPage(browser, link1)
    page.open()
    page.logo_click_main_page()


def test_rates_click_main_page(browser):
    page = MainPage(browser, link1)
    page.open()
    page.header_rates()


def test_catalog_click_main_page(browser):
    page = MainPage(browser, link1)
    page.open()
    page.header_catalog()


def test_gallery_click_main_page(browser):
    page = MainPage(browser, link1)
    page.open()
    page.header_gallery()


@pytest.mark.login_page
class Test_login_page:
    def test_should_be_login_window(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        #browser.execute_script("window.scrollBy(100, 0);")  # скролл страницы
        browser.windowMaximize()
        page.should_be_login_form()

    def test_there_must_be_input_fields(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        #browser.execute_script("window.scrollBy(100, 0);")
        browser.windowMaximize()
        page.there_must_be_input_fields()
