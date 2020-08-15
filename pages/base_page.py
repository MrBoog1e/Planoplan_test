class BasePage:
    # передаем экземпляр драйвера и url адрес
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # открывает нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)

    # ожидание элемента 10 секунд
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
