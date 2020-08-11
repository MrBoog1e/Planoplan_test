class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=30):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)