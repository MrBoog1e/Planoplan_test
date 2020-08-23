from selenium.webdriver.common.by import By


class YandexEmailLocators:
    login_button = (By.XPATH, '//*[@id="index-page-container"]/div/div[2]/div/div/div[4]/a[2]')
    input_email_yandex = (By.CSS_SELECTOR, 'input[name="login"]')
    enter_button1 = (By.CSS_SELECTOR, 'button[type="submit"]')
    input_password_yandex = (By.CSS_SELECTOR, 'input[type="password"]')
    enter_button2 = (By.CSS_SELECTOR, 'button[type="submit"]')
    message1 = (By.CSS_SELECTOR, 'span[title="Сброс пароля"]')
    message2 = (By.CSS_SELECTOR, 'span[title="Сброс пароля"]')