def new_user_registration(self):
    words = ['boogie', 'dance', 'every', 'day', 'every', 'night']
    for i in range(1):
        arr = random.sample(words, random.randint(1, 4))
        # select a random element from arr and append to self
        arr.append(random.choice(words))
        print('email=' + ''.join(arr) + '@ya.ru')
        print('password=' + ''.join(arr))

    self.browser.find_element(By.CLASS_NAME, 'link__View-sc-1ydrjtx-0.koEghb').click(), 'There is no register form '

    email1 = self.browser.find_element(By.CSS_SELECTOR, 'input[name="username"]'), 'No such element Email'
    email1.send_keys(''.join(arr) + '@ya.ru')
    password1 = self.browser.find_element(By.CSS_SELECTOR, 'input[name="password"]'), 'No such element Password'
    password1.send_keys(''.join(arr))
    self.browser.find_element(By.CLASS_NAME, 'button-action__View-sc-1xgnbfo-0.cCelhz').click()
