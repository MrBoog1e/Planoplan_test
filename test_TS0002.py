from .pages.login_page import User_registration
import pytest

link1 = "https://planoplan.com/"


class Test_User_registration_on_the_website:

    @pytest.mark.smoke
    @pytest.mark.CRNU_001
    def test_new_user_registration(self, browser):
        page = User_registration(browser, link1)
        page.open()
        page.header_login()
        page.new_user_in_correct_registration()

    @pytest.mark.CRNU_002
    def test_new_user_in_incorrect_registration(self, browser):
        page = User_registration(browser, link1)
        page.open()
        page.header_login()
        page.new_user_in_incorrect_registration()
