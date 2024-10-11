import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.clients_list_page import ClientsList
from pages.login import sms_center, base_password, base_lke
from pages.producers_list_page import ProducersList
from pages.registration_page import Registration
from pages.sidebar import SideBar
from pages.sms_center_page import SmsCenter


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Экспедитора: регистрация - Прямая, тлф. - '
                    '98+get_timestamp_eight_signs, инн - Рандом, лицо - Юридическое, почта - Etimestamp@mail.ru, '
                    'пользователь - Регресс Экс, после создания заходим в ЛК и проверяем ИНН')
@pytest.mark.parametrize('base_fixture', ['without_login'], indirect=True)
def test_registration_new_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, login = base_fixture
    
    # Переход к странице регистрации
    login.click_button(login.registration_button)
    
    reg = Registration(base.driver)
    # Выбор типа регистрации - Экспедитор
    reg.click_button(reg.expeditor_button)
    phone = "98" + reg.get_timestamp(eight=True)
    # Ввод номера телефона
    reg.input_in_field(reg.phone_input, phone, click_first=True)
    # Принятие политики конфиденциальности
    reg.click_button(reg.privacy_policy_checkbox)
    # Запрос кода подтверждения
    reg.click_button(reg.get_code_button)
    
    sms = SmsCenter(base.driver)
    # Открытие нового окна для получения кода подтверждения
    sms.driver.execute_script("window.open(arguments[0]);", sms.sms_url)
    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    
    # Ввод логина и пароля для доступа к СМС центру
    sms.input_in_field(sms.sms_login_input, sms_center["login"], safe=True)
    sms.input_in_field(sms.sms_password_input, sms_center["password"], safe=True)
    # Переход к деталям сообщений
    sms.click_button(sms.sms_login_button)
    sms.click_button(sms.detailing_button)
    # Получение кода подтверждения
    code = sms.get_confirmation_code(phone)
    
    base.driver.switch_to.window(windows[0])
    
    # Ввод кода подтверждения
    reg.input_in_field(reg.code_input, code)
    reg.click_button(reg.continue_button)
    
    email = f"E{base.get_timestamp()}@mail.ru"
    # Ввод email пользователя
    reg.input_in_field(reg.email_input, email)
    
    # Ввод данных пользователя
    reg.input_in_field(reg.user_name_input, "Экс")
    reg.input_in_field(reg.user_surname_input, "Регресс")
    reg.input_in_field(reg.password_input, base_password["password"], safe=True)
    reg.input_in_field(reg.repeat_password_input, base_password["password"], safe=True)
    
    # Генерация и ввод ИНН
    inn = reg.generate_inn("entity")
    reg.input_in_field(reg.inn_input, inn, click_first=True)
    # Завершение регистрации
    reg.click_button(reg.complete_button, do_assert=True)
    reg.click_button(reg.ok_button)
    
    # Вход в личный кабинет
    login.input_in_field(login.user_email_input, email, safe=True)
    login.input_in_field(login.password_input, base_password["password"], safe=True)
    login.click_button(login.login_button)
    # Проверка ИНН пользователя
    login.assert_element_text(login.assert_inn, reference_value=inn)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Грузовладельца: регистрация - По ссылке Экс, тлф. - '
                    '98+get_timestamp_eight_signs, инн - Рандом, лицо - Юридическое, почта - Etimestamp@mail.ru, '
                    'пользователь - Регресс ГВ, после создания заходим в ЛК и проверяем ИНН, '
                    'далее заходим в ЛК Экс и принимаем ГВ в контур Экс.,')
@pytest.mark.parametrize('base_fixture', ['via_link'], indirect=True)
def test_registration_new_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, login = base_fixture
    
    reg = Registration(base.driver)
    # Переход к регистрации нового аккаунта
    reg.click_button(reg.registration_new_account)
    # Выбор типа регистрации - Грузовладелец
    reg.click_button(reg.client_button)
    phone = "98" + reg.get_timestamp(eight=True)
    # Ввод номера телефона
    reg.input_in_field(reg.phone_input, phone, click_first=True)
    # Принятие политики конфиденциальности
    reg.click_button(reg.privacy_policy_checkbox)
    # Запрос кода подтверждения
    reg.click_button(reg.get_code_button)
    
    sms = SmsCenter(base.driver)
    # Открытие нового окна для получения кода подтверждения
    sms.driver.execute_script("window.open(arguments[0]);", sms.sms_url)
    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    
    # Ввод логина и пароля для доступа к СМС центру
    sms.input_in_field(sms.sms_login_input, sms_center["login"], safe=True)
    sms.input_in_field(sms.sms_password_input, sms_center["password"], safe=True)
    # Переход к деталям сообщений
    sms.click_button(sms.sms_login_button)
    sms.click_button(sms.detailing_button)
    # Получение кода подтверждения
    code = sms.get_confirmation_code(phone)
    
    base.driver.switch_to.window(windows[0])
    
    # Ввод кода подтверждения
    reg.input_in_field(reg.code_input, code)
    reg.click_button(reg.continue_button)
    
    email = f"E{base.get_timestamp()}@mail.ru"
    # Ввод email пользователя
    reg.input_in_field(reg.email_input, email)
    
    # Ввод данных пользователя
    reg.input_in_field(reg.user_name_input, "ГВ")
    reg.input_in_field(reg.user_surname_input, "Регресс")
    reg.input_in_field(reg.password_input, base_password["password"], safe=True)
    reg.input_in_field(reg.repeat_password_input, base_password["password"], safe=True)
    
    # Генерация и ввод ИНН
    inn = reg.generate_inn("entity")
    reg.input_in_field(reg.inn_input, inn, click_first=True)
    # Завершение регистрации
    reg.click_button(reg.complete_button, do_assert=True)
    reg.click_button(reg.ok_button)
    
    # Вход в личный кабинет
    login.input_in_field(login.user_email_input, email, safe=True)
    login.input_in_field(login.password_input, base_password["password"], safe=True)
    login.click_button(login.login_button)
    # Проверка ИНН пользователя
    login.assert_element_text(login.assert_inn, reference_value=inn)
    
    # Выход из личного кабинета
    sidebar = SideBar(base.driver)
    sidebar.click_button(sidebar.exit_button)
    
    # Вход в личный кабинет Экспедитора
    login.input_in_field(login.user_email_input, base_lke["email"], safe=True)
    login.input_in_field(login.password_input, base_lke["password"], safe=True)
    login.click_button(login.login_button)
    
    # Принятие Грузовладельца в контур Экспедитора
    sidebar.click_button(sidebar.sidebar_button)
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    client_list = ClientsList(base.driver)
    client_list.click_button(client_list.accept_button, wait="lst")
    base.verify_text_by_inn(inn_value=inn, reference_value="Нет договора")
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Перевозчика: регистрация - По ссылке Экс, тлф. - '
                    '98+get_timestamp_eight_signs, инн - Рандом, лицо - Юридическое, почта - Etimestamp@mail.ru, '
                    'пользователь - Регресс ПВ, после создания заходим в ЛК и проверяем ИНН, '
                    'далее заходим в ЛК Экс и принимаем ПВ в контур Экс.,')
@pytest.mark.parametrize('base_fixture', ['via_link'], indirect=True)
def test_registration_new_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, login = base_fixture
    
    reg = Registration(base.driver)
    # Переход к регистрации нового аккаунта
    reg.click_button(reg.registration_new_account)
    # Выбор типа регистрации - Перевозчик
    reg.click_button(reg.producer_button)
    phone = "98" + reg.get_timestamp(eight=True)
    # Ввод номера телефона
    reg.input_in_field(reg.phone_input, phone, click_first=True)
    # Принятие политики конфиденциальности
    reg.click_button(reg.privacy_policy_checkbox)
    # Запрос кода подтверждения
    reg.click_button(reg.get_code_button)
    
    sms = SmsCenter(base.driver)
    # Открытие нового окна для получения кода подтверждения
    sms.driver.execute_script("window.open(arguments[0]);", sms.sms_url)
    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    
    # Ввод логина и пароля для доступа к СМС центру
    sms.input_in_field(sms.sms_login_input, sms_center["login"], safe=True)
    sms.input_in_field(sms.sms_password_input, sms_center["password"], safe=True)
    # Переход к деталям сообщений
    sms.click_button(sms.sms_login_button)
    sms.click_button(sms.detailing_button)
    # Получение кода подтверждения
    code = sms.get_confirmation_code(phone)
    
    base.driver.switch_to.window(windows[0])
    
    # Ввод кода подтверждения
    reg.input_in_field(reg.code_input, code)
    reg.click_button(reg.continue_button)
    
    email = f"E{base.get_timestamp()}@mail.ru"
    # Ввод email пользователя
    reg.input_in_field(reg.email_input, email)
    
    # Ввод данных пользователя
    reg.input_in_field(reg.user_name_input, "ГВ")
    reg.input_in_field(reg.user_surname_input, "Регресс")
    reg.input_in_field(reg.password_input, base_password["password"], safe=True)
    reg.input_in_field(reg.repeat_password_input, base_password["password"], safe=True)
    
    # Генерация и ввод ИНН
    inn = reg.generate_inn("entity")
    reg.input_in_field(reg.inn_input, inn, click_first=True)
    # Завершение регистрации
    reg.click_button(reg.complete_button, do_assert=True)
    reg.click_button(reg.ok_button)
    
    # Вход в личный кабинет
    login.input_in_field(login.user_email_input, email, safe=True)
    login.input_in_field(login.password_input, base_password["password"], safe=True)
    login.click_button(login.login_button)
    # Проверка ИНН пользователя
    login.assert_element_text(login.assert_inn, reference_value=inn)
    
    # Выход из личного кабинета
    sidebar = SideBar(base.driver)
    sidebar.click_button(sidebar.exit_button)
    
    # Вход в личный кабинет Экспедитора
    login.input_in_field(login.user_email_input, base_lke["email"], safe=True)
    login.input_in_field(login.password_input, base_lke["password"], safe=True)
    login.click_button(login.login_button)
    
    # Принятие Перевозчика в контур Экспедитора
    sidebar.click_button(sidebar.sidebar_button)
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    producer_list = ProducersList(base.driver)
    producer_list.click_button(producer_list.accept_button, wait="lst")
    base.verify_text_by_inn(inn_value=inn, reference_value="Нет договора")
    # Конец теста
    