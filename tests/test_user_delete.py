import allure
import pytest
from pages.login import accounts
from pages.profile_page import Profile


@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКЭ. Тест удаления пользователя: пользователь - Первый в списке')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_user_delete_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

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
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКП. Тест удаления пользователя: пользователь - Первый в списке')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_user_delete_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

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
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКЗ. Тест удаления пользователя: пользователь - Первый в списке')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_user_delete_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

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
    # Конец теста
