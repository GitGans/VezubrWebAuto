import allure
from tests.base_test import base_test_with_login
from pages.profile_page import Profile
from pages.user_add_page import User


@allure.epic("Стабильные тесты")
@allure.story("Critical path test")
@allure.feature('Редактирование пользователей')
@allure.description('ЛКЗ. Тест редактирования пользователя: пользователь - Первый в списке, ФИО - ФИО-timestamp, '
                    'тип - API, роль - Логист, тлф - Рандом, email - Etimestamp@mail.ru. часовой пояс - Абиджан')
def test_user_edit_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True)
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
    user.backspace_len_and_input(user.phone_input, base.random_value_float_str(1000000000, 9999999999))
    user.backspace_len_and_input(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    user.click_button(user.save_edit_user_button, do_assert=True)
    user.click_button(user.confirm_add_button)

    sidebar.test_finish()
