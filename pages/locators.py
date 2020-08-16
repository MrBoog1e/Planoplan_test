from selenium.webdriver.common.by import By


class MainPageLocators:
    language_button = (By.CLASS_NAME, 'current-lang-button__View-sc-1icouzm-0.bJfmgT')
    ru_language = (By.CSS_SELECTOR, 'img[alt="Русский"]')
    en_language = (By.CSS_SELECTOR, 'img[alt="English"]')
    de_language = (By.CSS_SELECTOR, 'img[alt="Deutsch"]')
    su_language = (By.CSS_SELECTOR, 'img[alt="Suomi"]')
    po_language = (By.CSS_SELECTOR, 'img[alt="Português brasileiro"]')

    logo_planoplan = (By.CLASS_NAME, 'newpp_header__logo-img')
    header_rates = (By.CSS_SELECTOR, 'a[href*="/pricing/"]')
    header_catalog = (By.CSS_SELECTOR, 'a[href*="/catalog/"]')
    header_gallery = (By.CSS_SELECTOR, 'a[href*="/gallery/"]')
    header_login = (By.CLASS_NAME, 'widget-button__ButtonText-sc-7ezmr3-4.kGpZKe')

    header_dowload_win = (By.CLASS_NAME, 'downloadButton.ga-download-win')
    header_dowload_mac = (By.XPATH, '//*[@id="downloadstandalone"]/table/tbody/tr/td[3]/a[2]')

    header_menu_more = (By.CLASS_NAME, 'newpp_header__menu-item.newpp_header__menu-submenu-toggle')
    developer = (By.CLASS_NAME, 'newpp_header__menu-submenu-item')
    blog = (By.CLASS_NAME, 'newpp_header__menu-submenu-item')
    faq = (By.CLASS_NAME, 'newpp_header__menu-submenu-item')
    feedback = (By.CLASS_NAME, 'newpp_header__menu-submenu-item')
    download = (By.CLASS_NAME, 'newpp_header__menu-submenu-item')
    virtual_tours = (By.CLASS_NAME, 'newpp_header__menu-submenu-item')
    education = (By.CLASS_NAME, 'newpp_header__menu-submenu-item')


class LoginPageLocators:
    login_form = (By.CLASS_NAME, 'modal__Container-sc-1iesfw0-2.iqMAKd')
    input_email = (By.CSS_SELECTOR, 'input[type="email"]')
    input_password_new = (By.CSS_SELECTOR, 'input[autocomplete="new-password"]')
    input_password = (By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
    social_form = (By.CLASS_NAME, 'social__ButtonsGroup-qf4lof-2.hhRsyW')
    icon_vk = (By.CSS_SELECTOR, 'img[alt="Facebook"]')
    icon_fb = (By.CSS_SELECTOR, 'img[alt="Вконтакте"]')
    register_button = (By.CLASS_NAME, 'link__View-sc-1ydrjtx-0.koEghb')
    activation_message = (By.CLASS_NAME, 'modal__Container-sc-1iesfw0-2.iqMAKd')
    button_log_sign = (By.CLASS_NAME, 'button-action__View-sc-1xgnbfo-0.cCelhz')

