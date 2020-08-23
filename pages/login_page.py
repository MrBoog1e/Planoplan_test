from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .yandex_mail import YandexEmailLocators
from .locators import RegisterPageLocators
import random
import time


class User_authorization(BasePage):

    def header_login(self):
        button = self.browser.find_element(*MainPageLocators.header_login)
        button.click()

    def logins_with_correct_data(self):
        email = self.browser.find_element(*LoginPageLocators.input_email)
        email.send_keys('dm1try.zz@yandex.ru')
        password = self.browser.find_element(*LoginPageLocators.input_password)
        password.send_keys('starwars')
        self.browser.find_element(*LoginPageLocators.button_log_sign).click()
        time.sleep(4)
        assert "cabinet" in self.browser.current_url, "'cabinet' is not in current url. Link is not correct"

    def logins_with_invalid_data(self):
        email = self.browser.find_element(*LoginPageLocators.input_email)
        email.send_keys('dm1try.zz@yandex.ru')
        password = self.browser.find_element(*LoginPageLocators.input_password)
        password.send_keys('warsstar')
        self.browser.find_element(*LoginPageLocators.button_log_sign).click()
        assert self.browser.find_element(*LoginPageLocators.error_email_password), 'The error message did not appear'

    def authorization_when_the_password_is_lost(self):
        self.browser.find_element(*LoginPageLocators.forgot_password).click()
        time.sleep(2)
        email = self.browser.find_element(*LoginPageLocators.input_email)
        email.send_keys('dm1try.zz@yandex.ru')
        self.browser.find_element(*LoginPageLocators.forgot_button).click()
        # assert self.browser.find_element(*LoginPageLocators.input_check_your_email), 'Try in 5 minutes.'

    def authorization_on_Yandex_mail(self):
        self.browser.find_element(*YandexEmailLocators.login_button).click()
        email = self.browser.find_element(*YandexEmailLocators.input_email_yandex)
        email.send_keys('dm1try.zz')
        self.browser.find_element(*YandexEmailLocators.enter_button1).click()
        time.sleep(2)
        password = self.browser.find_element(*YandexEmailLocators.input_password_yandex)
        password.send_keys('starwars')
        self.browser.find_element(*YandexEmailLocators.enter_button2).click()
        assert self.browser.find_element(*YandexEmailLocators.message1), 'There is no message about password reset'


class User_registration(BasePage):

    def header_login(self):
        button = self.browser.find_element(*MainPageLocators.header_login)
        button.click()

    def new_user_in_correct_registration(self):
        global arr
        words = ['boog1e', 'dance', 'every2', '2day', 'every', 'n1ght']
        for i in range(1):
            arr = random.sample(words, random.randint(1, 4))
            # select a random element from arr and append to self
            arr.append(random.choice(words))
            print('email=' + ''.join(arr) + '@ya.ru')
            print('password=' + ''.join(arr))
        self.browser.find_element(*LoginPageLocators.button_log_sign).click()
        self.browser.find_element(*LoginPageLocators.register_button).click(), 'There is no register form '
        email1 = self.browser.find_element(*LoginPageLocators.input_email)
        email1.send_keys(''.join(arr) + '@ya.ru')
        time.sleep(1)
        password = self.browser.find_element(*LoginPageLocators.input_password_new)
        password.send_keys(''.join(arr))
        assert self.browser.find_element(
            *LoginPageLocators.activation_message), 'There is no Check your email form '

    def new_user_in_incorrect_registration(self):
        self.browser.find_element(*LoginPageLocators.register_button).click(), 'There is no register form '
        email1 = self.browser.find_element(*LoginPageLocators.input_email)
        email1.send_keys('dmitry.z111@yandex.11')
        password = self.browser.find_element(*LoginPageLocators.input_password_new)
        password.send_keys('starwars')
        assert self.browser.find_element(*RegisterPageLocators.error_message_email), 'Error mail is incorrect absent'
        assert self.browser.find_element(*RegisterPageLocators.button_register), 'The registration button is active'