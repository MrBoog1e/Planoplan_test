from .pages.login_page import User_authorization
import pytest

link1 = "https://planoplan.com/"
link2 = "https://mail.yandex.ru/"


class Test_User_authorization_on_the_website:

    @pytest.mark.smoke
    @pytest.mark.VACD_001
    def test_logins_with_correct_data(self, browser):
        page = User_authorization(browser, link1)
        page.open()
        page.header_login()
        page.logins_with_correct_data()

    @pytest.mark.VACD_002
    def test_logins_with_invalid_data(self, browser):
        page = User_authorization(browser, link1)
        page.open()
        page.header_login()
        page.logins_with_invalid_data()

    @pytest.mark.smoke
    @pytest.mark.VACD_003
    def test_authorization_when_the_password_is_lost(self, browser):
        page = User_authorization(browser, link1)
        page.open()
        page.header_login()
        page.authorization_when_the_password_is_lost()
        page = User_authorization(browser, link2)
        page.open()
        page.authorization_on_Yandex_mail()
