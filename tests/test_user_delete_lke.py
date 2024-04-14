import allure
from pages.login import accounts
from tests.base_test import base_test_with_login
from pages.profile_page import Profile


@allure.feature('Удаление пользователей')
@allure.description('ЛКЭ. Тест удаления пользователя: пользователь - Первый в списке')
def test_delete_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.users_tab, do_assert=True, wait="lst")
    profile.click_button_located(profile.delete_user_button)
    profile.input_in_field(profile.password_input, accounts["lke"]["password"], safe=True)
    profile.click_button(profile.delete_confirm_button, wait="lst", do_assert=True)

    sidebar.finish_test()
