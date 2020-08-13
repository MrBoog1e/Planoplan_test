import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose browser language")
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--start_maximized', action='store', default=None, help="full_size browser window")


@pytest.fixture(scope='function')
def browser(request, browser_name=None):
    user_language = request.config.getoption("language")
    if browser_name is None:
        browser_name = request.config.getoption("browser_name")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument('window-size=1600,1000')
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        assert browser_name == "chrome" or browser_name == "firefox", "You should choose browser: chrome or firefox"
    yield browser
    print("\nquit browser..")
    browser.quit()
