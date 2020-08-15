from .base_page import BasePage
from selenium.webdriver.common.by import By
import random
import time

class MainPage(BasePage):
    def changing_the_language_button_main_page(self):
        button = self.browser.find_element(By.CLASS_NAME, 'current-lang-button__View-sc-1icouzm-0.bJfmgT')
        button.click()
        assert self.browser.find_element(By.CSS_SELECTOR, 'img[alt="English"]'), 'English button is missing'
        assert self.browser.find_element(By.CSS_SELECTOR, 'img[alt="Русский"]'), 'Russian button is missing'
        assert self.browser.find_element(By.CSS_SELECTOR, 'img[alt="Deutsch"]'), 'Deutsch button is missing'
        assert self.browser.find_element(By.CSS_SELECTOR, 'img[alt="Suomi"]'), 'Suomi button is missing'
        assert self.browser.find_element(By.CSS_SELECTOR, 'img[alt="Português brasileiro"]'), 'Português button is ' \
                                                                                                 'missing '

    def logo_click_main_page(self):
        button = self.browser.find_element(By.CLASS_NAME, 'newpp_header__logo-img')
        button.click()

    def header_rates(self):
        button = self.browser.find_element(By.CSS_SELECTOR, 'a[href*="/pricing/"]')
        button.click()

    def header_catalog(self):
        button = self.browser.find_element(By.CSS_SELECTOR, 'a[href*="/catalog/"]')
        button.click()

    def header_gallery(self):
        button = self.browser.find_element(By.CSS_SELECTOR, 'a[href*="/gallery/"]')
        button.click()


class LoginPage(BasePage):

    def header_login(self):
        button = self.browser.find_element(By.CLASS_NAME, 'widget-button__ButtonText-sc-7ezmr3-4.kGpZKe')
        button.click()

    def should_be_login_form(self):
        assert self.browser.find_element(By.CLASS_NAME, 'modal__Container-sc-1iesfw0-2.iqMAKd'), 'There is no login ' \
                                                                                                 'form '

    def there_must_be_input_fields(self):
        assert self.browser.find_element(By.CSS_SELECTOR, 'input[type="email"]'), 'no email field '
        assert self.browser.find_element(By.CSS_SELECTOR, 'input[type="password"]'), 'no pass field '

    def there_must_be_social_form(self):
        assert self.browser.find_element(By.CLASS_NAME, 'social__ButtonsGroup-qf4lof-2.hhRsyW'), 'There is no social ' \
                                                                                                 'form '

    def there_must_be_social_form_icons(self):
        assert self.browser.find_element(By.CSS_SELECTOR, 'img[alt="Facebook"]'), 'There is no facebook icon '
        assert self.browser.find_element(By.CSS_SELECTOR, 'img[alt="Вконтакте"]'), 'There is no vk icon'


class UserAuthorization(BasePage):
    def header_login(self):
        button = self.browser.find_element(By.CLASS_NAME, 'widget-button__ButtonText-sc-7ezmr3-4.kGpZKe')
        button.click()

    def new_user_registration(self):
        global arr
        words = ['boogie', 'dance', 'every', 'day', 'every', 'night']
        for i in range(1):
            arr = random.sample(words, random.randint(1, 4))
            # select a random element from arr and append to self
            arr.append(random.choice(words))
            print('email=' + ''.join(arr) + '@ya.ru')
            print('password=' + ''.join(arr))

        self.browser.find_element(By.CLASS_NAME, 'link__View-sc-1ydrjtx-0.koEghb').click(), 'There is no register form '
        email1 = self.browser.find_element(By.CSS_SELECTOR, 'input[type="email"]')
        email1.send_keys(''.join(arr) + '@ya.ru')

        password = self.browser.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password.send_keys(''.join(arr))
        self.browser.find_element(By.CLASS_NAME, 'button-action__View-sc-1xgnbfo-0.cCelhz').click()
        assert self.browser.find_element(By.CLASS_NAME, 'modal__Container-sc-1iesfw0-2.iqMAKd'), 'There is no Check ' \
                                                                                                 'your email ' \
                                                                                                 'form '

    def user_login(self):
        email1 = self.browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        email1.send_keys('mrboog1e@ya.ru')
        password = self.browser.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
        password.send_keys('starwars')
        self.browser.find_element(By.CSS_SELECTOR, 'button[data-test="login_submit"]').click()
        time.sleep(1)
        assert "cabinet" in self.browser.current_url, "'cabinet' is not in current url. Link is not correct"
        assert self.browser.find_element(By.CLASS_NAME, 'sidebar__InnerSidebar-r1lxuc-3.huTqPB'), 'ERROR: No sidebar'
        assert self.browser.find_element(By.CLASS_NAME, 'page-layout__PageHeader-sc-1o3pawy-0.fGVXRJ'), 'ERROR: No ' \
                                                                                                        'PageHeader '
        assert self.browser.find_element(By.CLASS_NAME, 'page-layout__Content-sc-1o3pawy-5.imGmYI'), 'ERROR: No Content'

    def dowload_planoplan_main_page(self):
        button = self.browser.find_element(By.CLASS_NAME, 'downloadButton.ga-download-win')
        button.click()

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
