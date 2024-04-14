import allure
from tests.base_test import base_test_with_login
from pages.profile_page import Profile
from pages.user_add_page import User


@allure.feature('Создание пользователей')
@allure.description('ЛКЭ. Тест создания пользователя: ФИО - ФИО-timestamp, тип - Пользователь, роль - Админ, '
                    'тлф - Рандом, email - Etimestamp@mail.ru. часовой пояс - Екб, группа - Базовая группа, '
                    'подразделение - База')
def test_user_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True, wait="lst")
    profile.click_button(profile.add_group_button, wait="form")

    user = User(base.driver)
    user.dropdown_click_input_click(user.user_type_select, "Пользователь")
    user.dropdown_click_input_click(user.user_role_select, "Администратор")
    user.dropdown_click_input_click(user.user_timezone_select, "Asia/Yekaterinburg")
    user.input_in_field(user.surname_input, f"Ф-{base.get_timestamp()}")
    user.input_in_field(user.name_input, f"И-{base.get_timestamp()}")
    user.input_in_field(user.patronymic_input, f"О-{base.get_timestamp()}")
    user.click_button(user.phone_input)
    user.input_in_field(user.phone_input, base.random_value_int_str(1000000000, 9999999999))
    user.input_in_field(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    user.dropdown_click_input_click(user.user_group_select, "Базовая группа")
    user.dropdown_click_input_click(user.user_subdivision_select, "База")
    user.click_button(user.create_user_button, do_assert=True)
    user.click_button(user.confirm_add_button, wait="lst")

    sidebar.finish_test()
