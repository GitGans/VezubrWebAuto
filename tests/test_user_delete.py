import allure
from pages.login import accounts
from tests.base_test import base_test_with_login
from pages.profile_page import Profile


@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКЭ. Тест удаления пользователя: пользователь - Первый в списке')
def test_user_delete_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Клик по кнопке удаления пользователя
    profile.click_button(profile.delete_user_button, wait_type="located")
    # Ввод пароля для подтверждения удаления
    profile.input_in_field(profile.password_input, accounts["lke"]["password"], safe=True)
    # Подтверждение удаления пользователя
    profile.click_button(profile.delete_confirm_button, wait="lst", do_assert=True)

    # Завершение теста
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКП. Тест удаления пользователя: пользователь - Первый в списке')
def test_user_delete_lkp(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkp'
    base, sidebar = base_test_with_login(domain=domain, role='lkp')

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Клик по кнопке удаления пользователя
    profile.click_button(profile.delete_user_button, wait_type="located")
    # Ввод пароля для подтверждения удаления
    profile.input_in_field(profile.password_input, accounts["lkp"]["password"], safe=True)
    # Подтверждение удаления пользователя
    profile.click_button(profile.delete_confirm_button, wait="lst", do_assert=True)

    # Завершение теста
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКЗ. Тест удаления пользователя: пользователь - Первый в списке')
def test_user_delete_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    # Переход к профилю
    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    # Переход на вкладку пользователей
    profile.click_button(profile.users_tab, do_assert=True)
    # Клик по кнопке удаления пользователя
    profile.click_button(profile.delete_user_button, wait_type="located")
    # Ввод пароля для подтверждения удаления
    profile.input_in_field(profile.password_input, accounts["lkz"]["password"], safe=True)
    # Подтверждение удаления пользователя
    profile.click_button(profile.delete_confirm_button, wait="lst", do_assert=True)

    # Завершение теста
    sidebar.test_finish()
