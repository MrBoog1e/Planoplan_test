from .pages.main_page import MainPage, UserAuthorization
from .pages.main_page import LoginPage
import pytest
link1 = "https://planoplan.com/"
link2 = "https://mail.yandex.ru/"


@pytest.mark.header_menu
class Test_header_menu:
    def test_changing_the_language_button_main_page(self, browser):
        page = MainPage(browser, link1)
        page.open()
        page.changing_the_language_button_main_page()

    def test_logo_click_main_page(self, browser):
        page = MainPage(browser, link1)
        page.open()
        page.logo_click_main_page()

    def test_rates_click_main_page(self, browser):
        page = MainPage(browser, link1)
        page.open()
        page.header_rates()

    def test_catalog_click_main_page(self, browser):
        page = MainPage(browser, link1)
        page.open()
        page.header_catalog()

    def test_gallery_click_main_page(self, browser):
        page = MainPage(browser, link1)
        page.open()
        page.header_gallery()

    def test_header_dowload(self, browser):
        page = MainPage(browser, link1)
        page.open()
        page.header_dowload_win()
        page.header_dowload_mac()

    def test_header_menu_more(self, browser):
        page = MainPage(browser, link1)
        page.open()
        page.header_menu_more()


@pytest.mark.login_page
class Test_login_page:
    def test_should_be_login_window(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        # browser.execute_script("window.scrollBy(100, 0);")  # скролл страницы
        page.header_login()
        page.should_be_login_form()

    def test_there_must_be_input_fields(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        page.header_login()
        page.there_must_be_input_fields()

    def test_there_must_be_social_form(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        page.header_login()
        page.there_must_be_social_form()

