import allure
from tests.base_test import base_test_with_login
from pages.loader_add_page import LoaderAdd
from pages.loader_list_page import LoaderList


@allure.feature('Создание специалистов')
@allure.description('ЛКЭ. Тест создания специалиста Экс: ФИО - ФИО-timestamp, паспорт - РФ, тип - Грузчик, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом.')
def test_loader_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                                do_assert=True, wait="lst")

    loader_list = LoaderList(base.driver)
    loader_list.click_button(loader_list.add_loader_button, wait="form")

    add_loader = LoaderAdd(base.driver)
    add_loader.input_in_field(add_loader.surname_input, f"Ф-{base.get_timestamp()}")
    add_loader.input_in_field(add_loader.name_input, f"И-{base.get_timestamp()}")
    add_loader.input_in_field(add_loader.patronymic_input, f"О-{base.get_timestamp()}")
    add_loader.input_in_field(add_loader.passport_id_input, base.random_value_int_str(1000000000, 9999999999))
    add_loader.input_in_field(add_loader.passport_by_input, "Верховный грузила")
    add_loader.click_and_input_in_field(add_loader.passport_code_input, base.random_value_int_str(100000, 999999))
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Грузчик")
    add_loader.click_and_input_in_field(add_loader.app_phone_input, base.random_value_int_str(8650000000, 8659999999))
    add_loader.click_and_input_in_field(add_loader.contact_phone_input,
                                        base.random_value_int_str(8650000000, 8659999999))
    add_loader.input_in_field(add_loader.reg_address_input, "Мой адрес – Не дом и не улица")
    add_loader.input_in_field(add_loader.fact_address_input, "Мой адрес – Советский Союз.")
    add_loader.click_button(add_loader.create_loader_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="lst")

    sidebar.finish_test()
