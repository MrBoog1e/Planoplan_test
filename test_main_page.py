from .pages.main_page import MainPage, UserAuthorization
from .pages.main_page import LoginPage
import pytest
import time
link1 = "https://planoplan.com/"


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

    def test_there_must_be_social_form_icons(self, browser):
        page = LoginPage(browser, link1)
        page.open()
        page.header_login()
        page.there_must_be_social_form_icons()


@pytest.mark.smoke
class Test_new_user_functions:
    def test_new_user_registration(self, browser):
        page = UserAuthorization(browser, link1)
        page.open()
        page.header_login()
        page.new_user_registration()

    def test_login_user(self, browser):
        page = UserAuthorization(browser, link1)
        page.open()
        page.header_login()
        page.user_login()

    @pytest.mark.smoke1
    def test_dowload_planoplan_main_page(self,browser):
        page = UserAuthorization(browser, link1)
        page.open()
        page.dowload_planoplan_main_page()

    @pytest.mark.smoke2
    def test_shop_main_page(self, browser):
        page = UserAuthorization(browser, link1)
        page.open()
        page.header_login()
        page.user_login()
        page.shop_main_page()
