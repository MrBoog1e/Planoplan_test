Тестирование сайта Planoplan.com
Окружение: 1. Ubuntu: 20.04.1 LTS
           2. Google Chrome browser: 85.0.4183.59        
Маркеры:
* @pytest.mark.header_menu - проверка элементов заголовка;
* @pytest.mark.login_page - проверка элементов страницы логина;
* @pytest.mark.smoke - тестирование основных функций сайта.
Более углубленно в smoke:
* test_new_user_registration - регистрирует пользователя, путём случайно созданного логина/пароля, и проверят, появилась ли сообщение о том, что письмо подтверждение отправлено на почту;
* test_login_user - входит в личный кабинет, проверят корректность ссылки, и проверяет основные элементы для работы;
* dowload_planoplan_main_page - проверяет кликабельность кнопки, и сверку URL;
* shop_main_page - заранее созданный пользователь авторизуется на сайте, открывает корзину с главной страницы, добавляет товар , открывает корзину, проверяет кол-во добавлено товара, удаляет выбранную позицию (для повторного запуска теста), и проверят сообщение, есть ли предупреждение, что товара нет в корзине.
PS:**\ -в разработке, будет дополняться**
