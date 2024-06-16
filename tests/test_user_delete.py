import allure
from pages.login import accounts
from tests.base_test import base_test_with_login
from pages.profile_page import Profile


@allure.epic("Стабильные тесты")
@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКЭ. Тест удаления пользователя: пользователь - Первый в списке')
def test_user_delete_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True)
    profile.click_button(profile.delete_user_button, wait_type="located")
    profile.input_in_field(profile.password_input, accounts["lke"]["password"], safe=True)
    profile.click_button(profile.delete_confirm_button, wait="lst", do_assert=True)

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКП. Тест удаления пользователя: пользователь - Первый в списке')
def test_user_delete_lkp(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkp')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True)
    profile.click_button(profile.delete_user_button, wait_type="located")
    profile.input_in_field(profile.password_input, accounts["lkp"]["password"], safe=True)
    profile.click_button(profile.delete_confirm_button, wait="lst", do_assert=True)

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Critical path test")
@allure.feature('Удаление пользователей')
@allure.description('ЛКЗ. Тест удаления пользователя: пользователь - Первый в списке')
def test_user_delete_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True)
    profile.click_button(profile.delete_user_button, wait_type="located")
    profile.input_in_field(profile.password_input, accounts["lkz"]["password"], safe=True)
    profile.click_button(profile.delete_confirm_button, wait="lst", do_assert=True)

    sidebar.test_finish()
