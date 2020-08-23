from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import random
import time


class MainPage(BasePage):
    def changing_the_language_button_main_page(self):
        button = self.browser.find_element(*MainPageLocators.language_button)
        button.click()
        assert self.browser.find_element(*MainPageLocators.en_language), 'English button is missing'
        assert self.browser.find_element(*MainPageLocators.ru_language), 'Russian button is missing'
        assert self.browser.find_element(*MainPageLocators.de_language), 'Deutsch button is missing'
        assert self.browser.find_element(*MainPageLocators.su_language), 'Suomi button is missing'
        assert self.browser.find_element(*MainPageLocators.po_language), 'Português button is missing'

    def logo_click_main_page(self):
        button = self.browser.find_element(*MainPageLocators.logo_planoplan)
        button.click()

    def header_rates(self):
        button = self.browser.find_element(*MainPageLocators.header_rates)
        button.click()

    def header_catalog(self):
        button = self.browser.find_element(*MainPageLocators.header_catalog)
        button.click()

    def header_gallery(self):
        button = self.browser.find_element(*MainPageLocators.header_gallery)
        button.click()

    def header_dowload_win(self):
        button = self.browser.find_element(*MainPageLocators.header_dowload_win)
        button.click()

    def header_dowload_mac(self):
        button = self.browser.find_element(*MainPageLocators.header_dowload_mac)
        button.click()

    def header_menu_more(self):
        button = self.browser.find_element(*MainPageLocators.header_menu_more)
        button.click()
        assert self.browser.find_element(*MainPageLocators.blog)
        assert self.browser.find_element(*MainPageLocators.faq)
        assert self.browser.find_element(*MainPageLocators.feedback)
        assert self.browser.find_element(*MainPageLocators.download)
        assert self.browser.find_element(*MainPageLocators.virtual_tours)
        assert self.browser.find_element(*MainPageLocators.education)


class LoginPage(BasePage):
    def header_login(self):
        button = self.browser.find_element(*MainPageLocators.header_login)
        button.click()

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.login_form), 'There is no login form'

    def there_must_be_input_fields(self):
        assert self.browser.find_element(*LoginPageLocators.input_email), 'no email field '
        assert self.browser.find_element(*LoginPageLocators.input_password), 'no pass field '

    def there_must_be_social_form(self):
        assert self.browser.find_element(*LoginPageLocators.social_form), 'There is no social form'
        assert self.browser.find_element(*LoginPageLocators.icon_fb), 'There is no facebook icon'
        assert self.browser.find_element(*LoginPageLocators.icon_vk), 'There is no vk icon'

    def register_button(self):
        assert self.browser.find_element(*LoginPageLocators.register_button)


class UserAuthorization(BasePage):
    def header_login(self):
        button = self.browser.find_element(*MainPageLocators.header_login)
        button.click()

    def new_user_registration(self):
        global arr
        words = ['boogie1', '1dance', 'every1', '1day', 'every1', '1night']
        for i in range(1):
            arr = random.sample(words, random.randint(1, 4))
            # select a random element from arr and append to self
            arr.append(random.choice(words))
            print('email=' + ''.join(arr) + '@ya.ru')
            print('password=' + ''.join(arr))

        self.browser.find_element(*LoginPageLocators.register_button).click(), 'There is no register form '
        email1 = self.browser.find_element(*LoginPageLocators.input_email)
        email1.send_keys(''.join(arr) + '@ya.ru')
        password = self.browser.find_element(*LoginPageLocators.input_password_new)
        password.send_keys(''.join(arr))
        self.browser.find_element(*LoginPageLocators.button_log_sign).click()
        assert self.browser.find_element(*LoginPageLocators.activation_message), 'There is no Check your email form '

    def user_login(self):
        email1 = self.browser.find_element(*LoginPageLocators.input_email)
        email1.send_keys('mrboog1e@ya.ru')
        password = self.browser.find_element(*LoginPageLocators.input_password)
        password.send_keys('starwars')
        self.browser.find_element(*LoginPageLocators.button_log_sign).click()
        time.sleep(2)
        assert "cabinet" in self.browser.current_url, "'cabinet' is not in current url. Link is not correct"
        assert self.browser.find_element(By.CLASS_NAME, 'sidebar__InnerSidebar-r1lxuc-3.huTqPB'), 'ERROR: No sidebar'
        assert self.browser.find_element(By.CLASS_NAME, 'page-layout__PageHeader-sc-1o3pawy-0.fGVXRJ'), 'ERROR: No ' \
                                                                                                        'PageHeader '
        assert self.browser.find_element(By.CLASS_NAME, 'page-layout__Content-sc-1o3pawy-5.imGmYI'), 'ERROR: No Content'

    def shop_main_page(self):
        self.browser.find_element(By.CSS_SELECTOR, 'img[class="newpp_header__logo-img"]').click()
        self.browser.find_element(By.CLASS_NAME,
                                  'widget-button__ButtonText-sc-7ezmr3-4.kGpZKe').click(), 'ERROR: No SHOP BUTTON'
        self.browser.find_element(By.CSS_SELECTOR, 'button[data-test="quantity__add"]').click()
        self.browser.find_element(By.CSS_SELECTOR, 'button[data-test="card__button-in-cart"]').click()
        self.browser.find_element(By.CSS_SELECTOR, 'path[fill-rule="evenodd"]').click()
        basket = self.browser.find_element(By.CSS_SELECTOR, 'div[data-test="quantity__count"]')
        print('items in the basket:', basket.text)
        assert '2' == basket.text, 'There are more than two items in the basket'
        self.browser.find_element(By.CSS_SELECTOR, 'button[data-test="cart__item-remove"]').click()
        assert self.browser.find_element(By.CSS_SELECTOR, 'div[class="cart__Text-qkkyd4-1 gqYXXX"]'), 'no message: ' \
                                                                                                      'there are no ' \
                                                                                                      'products In ' \
                                                                                                      'your cart yet '