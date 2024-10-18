import allure
import pytest
from pages.profile_page import Profile
from pages.user_add_page import User


@allure.story("Smoke test")
@allure.feature('Создание пользователей')
@allure.description('ЛКЭ. Тест создания пользователя: ФИО - ФИО-timestamp, тип - Пользователь, роль - Админ, '
                    'тлф - Рандом, email - Etimestamp@mail.ru, часовой пояс - Екб, группа - Базовая группа, '
                    'подразделение - База')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_user_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Клик по кнопке добавления пользователя
    profile.click_button(profile.add_user_button)

    user = User(base.driver)
    # Выбор типа пользователя "Пользователь"
    user.dropdown_without_input(user.user_type_select, "Пользователь")
    # Выбор роли пользователя "Администратор"
    user.dropdown_without_input(user.user_role_select, "Администратор")
    # Выбор часового пояса "Asia/Yekaterinburg"
    user.dropdown_without_input(user.user_timezone_select, "Asia/Yekaterinburg")
    # Ввод фамилии пользователя
    user.input_in_field(user.surname_input, f"Ф-{base.get_timestamp()}")
    # Ввод имени пользователя
    user.input_in_field(user.name_input, f"И-{base.get_timestamp()}")
    # Ввод отчества пользователя
    user.input_in_field(user.patronymic_input, f"О-{base.get_timestamp()}")
    # Ввод номера телефона пользователя
    user.click_button(user.phone_input)
    user.input_in_field(user.phone_input, base.random_value_float_str(1000000000, 9999999999))
    # Ввод email пользователя
    user.input_in_field(user.email_input, f"E{base.get_timestamp()}@mail.ru")
    # Выбор группы пользователя "Базовая группа"
    user.dropdown_without_input(user.user_group_select, "Базовая группа")
    # Выбор подразделения пользователя "База"
    user.dropdown_without_input(user.user_subdivision_select, "База")
    # Клик по кнопке создания пользователя
    user.click_button(user.create_user_button, do_assert=True)
    # Подтверждение создания пользователя
    user.click_button(user.confirm_add_button)
    # Конец теста
