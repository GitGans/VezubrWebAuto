import allure
from tests.base_test import base_test
from pages.group_page import Group
from pages.profile_page import Profile


@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест создания группы: имя - №-timestamp, тип - Признак договора, признак - Рандом')
def test_group_attr_add_lke(domain):
    base, sidebar = base_test(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.groups_tab, wait="lst")
    profile.click_button(profile.add_group_button)

    group = Group(base.driver)
    group.input_in_field(group.title_input, f"№-{base.get_timestamp()}")
    group.dropdown_click_input_click(group.group_type_select, "Признак Договора")
    group.input_in_field(group.params_input, group.random_value_int_str(100, 5000))
    group.click_button(group.create_group_button, do_assert=True)
    group.click_button(group.confirm_add_button, wait="lst")

    sidebar.finish_test()


@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест создания группы: имя - №-timestamp, тип - Заказчик, заказчик - Рандом')
def test_group_client_add_lke(domain):
    base, sidebar = base_test(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.groups_tab, wait="lst")
    profile.click_button(profile.add_group_button)

    group = Group(base.driver)
    group.input_in_field(group.title_input, f"№-{base.get_timestamp()}")
    group.dropdown_click_input_click(group.group_type_select, "Заказчик")
    group.input_in_field(group.params_input, group.random_value_int_str(100, 5000))
    group.click_button(group.create_group_button, do_assert=True)
    group.click_button(group.confirm_add_button, wait="lst")

    sidebar.finish_test()


@allure.feature('Удаление групп')
@allure.description('ЛКЭ. Тест удалания группы: группа - Шестая в списке')
def test_group_delete_lke(domain):
    base, sidebar = base_test(domain=domain, role='lke')

    sidebar.click_button(sidebar.profile_button, do_assert=True)

    profile = Profile(base.driver)
    profile.click_button(profile.groups_tab, wait="lst")
    profile.click_button(profile.groups_delete_button)
    profile.click_button(profile.confirm_button, wait="lst")

    sidebar.finish_test()
