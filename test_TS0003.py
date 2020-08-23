from .pages.shop_page import Shop
import pytest

link1 = "https://planoplan.com/"


class Test_shopping_page:

    @pytest.mark.smoke
    @pytest.mark.CHSW_001
    def test_performance_of_the_basket(self, browser):
        page = Shop(browser, link1)
        page.open()
        page.user_login_shopping()
        page.performance_of_the_basket()

    @pytest.mark.CHSW_002
    def test_performance_tariff_plan(self, browser):
        page = Shop(browser, link1)
        page.open()
        page.user_login_shopping()
        page.performance_tariff_plan()
