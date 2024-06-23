import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.clients_list_page import ClientsList
from pages.login import sms_center, base_password, base_lke
from pages.producers_list_page import ProducersList
from pages.registration_page import Registration
from pages.sidebar import SideBar
from pages.sms_center_page import SmsCenter
from tests.base_test import base_test_without_login, base_test_with_login_via_link


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Экспедитора: регистрация - Прямая, тлф. - '
                    '98+get_timestamp_eight_signs, инн - Рандом, лицо - Юридическое, почта - Etimestamp@mail.ru, '
                    'пользователь - Регресс Экс, после создания заходим в ЛК и проверяем ИНН')
def test_registration_new_lke(domain):
    base, login = base_test_without_login(domain=domain)

    login.click_button(login.registration_button)

    reg = Registration(base.driver)
    reg.click_button(reg.expeditor_button)
    phone = "98" + reg.get_timestamp_eight_signs()
    reg.input_in_field(reg.phone_input, phone, click_first=True)
    reg.click_button(reg.privacy_policy_checkbox)
    reg.click_button(reg.get_code_button)

    sms = SmsCenter(base.driver)
    sms.driver.execute_script("window.open(arguments[0]);", sms.sms_url)

    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])

    sms.input_in_field(sms.sms_login_input, sms_center["login"], safe=True)
    sms.input_in_field(sms.sms_password_input, sms_center["password"], safe=True)
    sms.click_button(sms.sms_login_button)
    sms.click_button(sms.detailing_button)
    code = sms.get_confirmation_code(phone)

    base.driver.switch_to.window(windows[0])

    reg.input_in_field(reg.code_input, code)
    reg.click_button(reg.continue_button)

    email = f"E{base.get_timestamp()}@mail.ru"
    reg.input_in_field(reg.email_input, email)

    reg.input_in_field(reg.user_name_input, "Экс")
    reg.input_in_field(reg.user_surname_input, "Регресс")
    reg.input_in_field(reg.password_input, base_password["password"], safe=True)
    reg.input_in_field(reg.repeat_password_input, base_password["password"], safe=True)

    inn = reg.generate_inn("entity")
    reg.input_in_field(reg.inn_input, inn, click_first=True)
    reg.click_button(reg.complete_button, do_assert=True)
    reg.click_button(reg.ok_button)

    login.input_in_field(login.user_email_input, email, safe=True)
    login.input_in_field(login.password_input, base_password["password"], safe=True)
    login.click_button(login.login_button)
    login.flexible_assert_word(login.assert_inn, reference_value=inn)

    base.test_finish()


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Грузовледельца: регистрация - По ссылке Экс, тлф. - '
                    '98+get_timestamp_eight_signs, инн - Рандом, лицо - Юридическое, почта - Etimestamp@mail.ru, '
                    'пользователь - Регресс ГВ, после создания заходим в ЛК и проверяем ИНН, '
                    'далее заходим в ЛК Экс и принимаем ГВ в контур Экс.,')
def test_registration_new_lkz(domain):
    base, login = base_test_with_login_via_link(domain=domain)

    reg = Registration(base.driver)
    reg.click_button(reg.registration_new_account)
    reg.click_button(reg.client_button)
    phone = "98" + reg.get_timestamp_eight_signs()
    reg.input_in_field(reg.phone_input, phone, click_first=True)
    reg.click_button(reg.privacy_policy_checkbox)
    reg.click_button(reg.get_code_button)

    sms = SmsCenter(base.driver)
    sms.driver.execute_script("window.open(arguments[0]);", sms.sms_url)

    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])

    sms.input_in_field(sms.sms_login_input, sms_center["login"], safe=True)
    sms.input_in_field(sms.sms_password_input, sms_center["password"], safe=True)
    sms.click_button(sms.sms_login_button)
    sms.click_button(sms.detailing_button)
    code = sms.get_confirmation_code(phone)

    base.driver.switch_to.window(windows[0])

    reg.input_in_field(reg.code_input, code)
    reg.click_button(reg.continue_button)

    email = f"E{base.get_timestamp()}@mail.ru"
    reg.input_in_field(reg.email_input, email)

    reg.input_in_field(reg.user_name_input, "ГВ")
    reg.input_in_field(reg.user_surname_input, "Регресс")
    reg.input_in_field(reg.password_input, base_password["password"], safe=True)
    reg.input_in_field(reg.repeat_password_input, base_password["password"], safe=True)

    inn = reg.generate_inn("entity")
    reg.input_in_field(reg.inn_input, inn, click_first=True)
    reg.click_button(reg.complete_button, do_assert=True)
    reg.click_button(reg.ok_button)

    login.input_in_field(login.user_email_input, email, safe=True)
    login.input_in_field(login.password_input, base_password["password"], safe=True)
    login.click_button(login.login_button)
    login.flexible_assert_word(login.assert_inn, reference_value=inn)

    sidebar = SideBar(base.driver)
    sidebar.click_button(sidebar.exit_button)

    login.input_in_field(login.user_email_input, base_lke["email"], safe=True)
    login.input_in_field(login.password_input, base_lke["password"], safe=True)
    login.click_button(login.login_button)

    sidebar.click_button(sidebar.sidebar_button)
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    client_list.click_button(client_list.accept_button)
    base.verify_text_by_inn(inn_value=inn, reference_value="Нет договора")
    
    time.sleep(1)

    base.test_finish()


@allure.story("Smoke test")
@allure.feature('Регистрация личного кабинета')
@allure.description('Тест регистрации личного кабинета Перевозчика: регистрация - По ссылке Экс, тлф. - '
                    '98+get_timestamp_eight_signs, инн - Рандом, лицо - Юридическое, почта - Etimestamp@mail.ru, '
                    'пользователь - Регресс ПВ, после создания заходим в ЛК и проверяем ИНН, '
                    'далее заходим в ЛК Экс и принимаем ПВ в контур Экс.,')
def test_registration_new_lkp(domain):
    base, login = base_test_with_login_via_link(domain=domain)

    reg = Registration(base.driver)
    reg.click_button(reg.registration_new_account)
    reg.click_button(reg.producer_button)
    phone = "98" + reg.get_timestamp_eight_signs()
    reg.input_in_field(reg.phone_input, phone, click_first=True)
    reg.click_button(reg.privacy_policy_checkbox)
    reg.click_button(reg.get_code_button)

    sms = SmsCenter(base.driver)
    sms.driver.execute_script("window.open(arguments[0]);", sms.sms_url)

    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])

    sms.input_in_field(sms.sms_login_input, sms_center["login"], safe=True)
    sms.input_in_field(sms.sms_password_input, sms_center["password"], safe=True)
    sms.click_button(sms.sms_login_button)
    sms.click_button(sms.detailing_button)
    code = sms.get_confirmation_code(phone)

    base.driver.switch_to.window(windows[0])

    reg.input_in_field(reg.code_input, code)
    reg.click_button(reg.continue_button)

    email = f"E{base.get_timestamp()}@mail.ru"
    reg.input_in_field(reg.email_input, email)

    reg.input_in_field(reg.user_name_input, "ГВ")
    reg.input_in_field(reg.user_surname_input, "Регресс")
    reg.input_in_field(reg.password_input, base_password["password"], safe=True)
    reg.input_in_field(reg.repeat_password_input, base_password["password"], safe=True)

    inn = reg.generate_inn("entity")
    reg.input_in_field(reg.inn_input, inn, click_first=True)
    reg.click_button(reg.complete_button, do_assert=True)
    reg.click_button(reg.ok_button)

    login.input_in_field(login.user_email_input, email, safe=True)
    login.input_in_field(login.password_input, base_password["password"], safe=True)
    login.click_button(login.login_button)
    login.flexible_assert_word(login.assert_inn, reference_value=inn)

    sidebar = SideBar(base.driver)
    sidebar.click_button(sidebar.exit_button)

    login.input_in_field(login.user_email_input, base_lke["email"], safe=True)
    login.input_in_field(login.password_input, base_lke["password"], safe=True)
    login.click_button(login.login_button)

    sidebar.click_button(sidebar.sidebar_button)
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.click_button(producer_list.accept_button)
    base.verify_text_by_inn(inn_value=inn, reference_value="Нет договора")
    
    time.sleep(1)

    base.test_finish()
