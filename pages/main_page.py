from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def changing_the_language_button_main_page(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="cabinet-widget"]/div/div/div/button/img')
        button.click()

    def logo_click_main_page(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="header"]/div/div/a/img')
        button.click()

    def header_rates(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div[1]/a[1]')
        button.click()

    def header_catalog(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div[1]/a[2]')
        button.click()

    def header_gallery(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="header"]/div/div/div[1]/a[3]')
        button.click()

    def header_login(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="cabinet-widget"]/div/a/span')
        button.click()


class LoginPage(BasePage):
    def should_be_login_form(self):
        button = self.browser.find_element(By.XPATH, '//*[@id="cabinet-widget"]/div/a/span')
        button.click()
        assert self.browser.find_element(By.XPATH, '//*[@id="form-entry"]'), 'There is no login form'

    def there_must_be_input_fields (self):
        button = self.browser.find_element(By.XPATH, '//*[@id="cabinet-widget"]/div/a/span')
        button.click()
        assert self.browser.find_element(By.XPATH, '//*[@id="form-entry"]/div/form/fieldset[1]/label/div[2]/input'), 'no email field'
        assert self.browser.find_element(By.XPATH, '//*[@id="form-entry"]/div/form/fieldset[2]/label/div[2]/input'), 'no password field'
