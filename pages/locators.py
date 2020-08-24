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
    input_password_new = (By.CLASS_NAME, 'input__InputHtml-sc-185agi7-3.ipRijx')
    input_password = (By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
    social_form = (By.CLASS_NAME, 'social__ButtonsGroup-qf4lof-2.hhRsyW')
    icon_vk = (By.CSS_SELECTOR, 'img[alt="Facebook"]')
    icon_fb = (By.CSS_SELECTOR, 'img[alt="Вконтакте"]')
    register_form = (By.CSS_SELECTOR, 'button[data-test="button_signup"]')
    register_button = (By.CSS_SELECTOR, 'button[data-test="signup_submit"]')
    activation_message = (By.CSS_SELECTOR, 'input[name="code"]')
    button_log_sign = (By.CLASS_NAME, 'button-action__View-sc-1xgnbfo-0.cCelhz')
    error_email_password = (By.CSS_SELECTOR, 'div[data-test="error-message"]')
    forgot_password = (By.CSS_SELECTOR, 'button[data-test="button_forgot-pass"]')
    forgot_button = (By.CLASS_NAME, 'buttonLoader__View-hkgzw7-0.iWHvdP')
    input_check_your_email = (By.CSS_SELECTOR, 'input[name="code"]')


class RegisterPageLocators:
    error_message_email = (By.CLASS_NAME, 'input__Error-sc-185agi7-5.bjJczZ')
    button_register = (By.CLASS_NAME, 'buttonLoader__View-hkgzw7-0.beSJaU')


class ShopPageLocators:
    shop_button = (By.CSS_SELECTOR, 'a[data-test="widget__button-store"]')
    overview_button = (By.CSS_SELECTOR, 'button[data-test="sidebar__button-REVIEW"]')
    packages_button = (By.CSS_SELECTOR, 'button[data-test="sidebar__button-PACKAGES"]')
    render_button = (By.CSS_SELECTOR, 'button[data-test="sidebar__button-RENDERS"]')
    panoramas_button = (By.CSS_SELECTOR, 'button[data-test="sidebar__button-PANORAMAS"]')
    widget_button = (By.CSS_SELECTOR, 'button[data-test="sidebar__button-WIDGET"]')
    plans_button = (By.CSS_SELECTOR, 'button[data-test="sidebar__button-PRICING"]')
    #/packages
    plus_button = (By.CSS_SELECTOR, 'button[data-test="quantity__add"]')
    minus_button = (By.CSS_SELECTOR, 'button[data-test="quantity__remove"]')
    add_to_card = (By.CSS_SELECTOR, 'button[data-test="card__button-in-cart"]')
    basket_button = (By.CSS_SELECTOR, 'button[data-test="sidebar__cart-button"]')
    basket_amount_product = (By.CSS_SELECTOR, 'div[data-test="quantity__count"]')
    remove_product = (By.CSS_SELECTOR, 'button[data-test="cart__item-remove"]')
    message_empty_bucket = (By.CSS_SELECTOR, 'div[class="cart__Text-qkkyd4-1 gqYXXX"]')
    #/plans
    chose_plans_button = (By.CSS_SELECTOR, 'a[data-test="pricing__button-upgrade"]')
    tariff_name = (By.CSS_SELECTOR, 'div[data-test="tariff_name"]')
