from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import ShopPageLocators
import time


class Shop(BasePage):

    def user_login_shopping(self):
        self.browser.find_element(*MainPageLocators.header_login).click()
        email = self.browser.find_element(*LoginPageLocators.input_email)
        email.send_keys('dm1try.zz@yandex.ru')
        password = self.browser.find_element(*LoginPageLocators.input_password)
        password.send_keys('starwars')
        self.browser.find_element(*LoginPageLocators.button_log_sign).click()
        self.browser.find_element(*ShopPageLocators.shop_button).click()

    def performance_of_the_basket(self):
        self.browser.find_element(*ShopPageLocators.packages_button).click()
        self.browser.find_element(*ShopPageLocators.plus_button).click()
        self.browser.find_element(*ShopPageLocators.add_to_card).click()
        self.browser.find_element(*ShopPageLocators.basket_button).click()
        basket_amout = self.browser.find_element(*ShopPageLocators.basket_amount_product)
        assert '2' == basket_amout.text, 'There are more than two items in the basket'
        self.browser.find_element(*ShopPageLocators.remove_product).click()
        assert self.browser.find_element(*ShopPageLocators.message_empty_bucket), 'no message: there are no products ' \
                                                                                  'In your cart yet '

    def performance_tariff_plan(self):
        self.browser.find_element(*ShopPageLocators.plans_button).click()
        self.browser.find_element(*ShopPageLocators.chose_plans_button).click()
        time.sleep(1)
        assert "tariff-managment" in self.browser.current_url, "'tariff-managment' is not in current url"
        tariff_name = self.browser.find_element(*ShopPageLocators.tariff_name)
        assert 'PRO' == tariff_name.text, 'The fare name does not match the one you selected'
