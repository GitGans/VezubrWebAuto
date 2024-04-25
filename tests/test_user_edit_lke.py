import time
import allure
from tests.base_test import base_test_with_login
from pages.profile_page import Profile
from pages.user_add_page import User


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Редактирование пользователей')
@allure.description('ЛКЭ. Тест редактирования пользователя: пользователь - Первый в списке, ФИО - ФИО-timestamp, '
                    'тип - API, роль - Логист, тлф - Рандом, email - Etimestamp@mail.ru. часовой пояс - Абиджан')
def test_first_user_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True, wait="lst")
    profile.click_button(profile.user_link, wait="form")

    user = User(base.driver)
    user.click_button(user.user_edit_button, wait="form")
    user.dropdown_click_input_click(user.user_type_select, "API")
    user.click_button(user.user_role_reset)
    user.dropdown_click_input_click(user.user_role_select, "Логист")
    user.dropdown_click_input_click(user.user_timezone_select, "Africa/Abidjan")
    user.backspace_len_and_input(user.surname_input, f"Ф-{base.get_timestamp()}")
    user.backspace_len_and_input(user.name_input, f"И-{base.get_timestamp()}")
    user.backspace_len_and_input(user.patronymic_input, f"О-{base.get_timestamp()}")
    user.click_button(user.phone_input)
    user.backspace_len_and_input(user.phone_input, base.random_value_int_str(1000000000, 9999999999))
    user.backspace_len_and_input(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    user.click_button(user.save_edit_user_button, do_assert=True)
    user.click_button(user.confirm_add_button, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Редактирование пользователей')
@allure.description('ЛКЭ. Тест управления ответственностью за КА: пользователь - Второй в списке, '
                    'назначение на ГВ - Все, делигировать - Шестому, отвязать - Всех.')
def test_user_responsible_fo_client_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True, wait="lst")
    profile.click_button_index(profile.user_link, 2, wait="form")

    user = User(base.driver)
    user.click_button(user.add_responsible_button, wait="lst")
    user.click_button(user.all_client_on_checkbox)
    user.click_button(user.confirm_responsible_button, wait="lst")

    user.click_button(user.all_contractor_off_checkbox)
    user.click_button(user.delegate_responsibility_button, wait="lst")
    user.click_button_index(user.user_checkbox, 7)
    user.click_button(user.confirm_responsible_button, wait="lst")

    user.click_button(user.all_contractor_off_checkbox)
    user.click_button(user.off_responsibility_button)
    user.click_button(user.confirm_off_responsible_button, wait="lst", do_assert=True)

    sidebar.finish_test()

@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Редактирование пользователей')
@allure.description('ЛКЭ. Тест управления ответственностью за КА: пользователь - Первый в списке, '
                    'назначение на ПВ - Все, делигировать - Пятому, отвязать - Всех.')
def test_user_responsible_fo_producer_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True, wait="lst")
    profile.click_button(profile.user_link, wait="form")

    user = User(base.driver)
    user.click_button(user.add_responsible_button, wait="lst")
    user.click_button(user.producer_tab, wait="lst")
    time.sleep(2)
    user.click_button(user.all_producer_on_checkbox)
    user.click_button(user.confirm_responsible_button, wait="lst")

    user.click_button(user.contractor_role_select)
    user.click_button(user.select_producer, wait="lst")

    user.click_button(user.all_contractor_off_checkbox)
    user.click_button(user.delegate_responsibility_button, wait="lst")
    user.click_button_index(user.user_checkbox, 6)
    user.click_button(user.confirm_responsible_button, wait="lst")

    user.click_button(user.all_contractor_off_checkbox)
    user.click_button(user.off_responsibility_button)
    user.click_button(user.confirm_off_responsible_button, wait="lst", do_assert=True)

    sidebar.finish_test()
