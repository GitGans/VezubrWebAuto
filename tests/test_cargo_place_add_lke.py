import time
import allure
from tests.base_test import base_test_with_login
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.feature('Создание грузомест')
@allure.description('ЛКЭ. Тест создания ГМ ГВ: '
                    'тип - Короб, вес/объем/цена - Рандом, статус - Новое, адреса - Первые из списка.')
def test_cargo_place_from_lkz_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.assignments_list_button,
                                do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    add_cp.dropdown_click_input_click(add_cp.cargo_place_owner_select, "Auto LKZ")
    add_cp.dropdown_click_input_click(add_cp.lke_cp_type_select, "Короб")
    add_cp.input_in_field(add_cp.cp_weight_input, base.random_value_int_str(10, 20000))
    add_cp.input_in_field(add_cp.cp_value_input, base.random_value_float_str(0.1, 35.0))
    add_cp.input_in_field(add_cp.cp_cost_input, base.random_value_int_str(100, 1000000))
    add_cp.dropdown_click_input_click(add_cp.lke_cp_status_select, "Новое")
    add_cp.dropdown_click_input_enter(add_cp.departure_address_select, "Auto LKZ")
    add_cp.dropdown_click_input_enter(add_cp.delivery_address_select, "Auto LKZ")
    add_cp.click_button(add_cp.create_cargo_place_button, do_assert=True)
    add_cp.click_button(add_cp.confirm_add_button, wait="lst")

    sidebar.finish_test()


@allure.feature('Создание грузомест')
@allure.description('ЛКЭ. Тест создания ГМ Экс с вложеными ГМ ГВ: '
                    'ГМ - Первое, тип - Короб, вес/объем/цена - Рандом, статус - Новое, адреса - Первые из списка.')
def test_cargo_place_own_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.assignments_list_button,
                                do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    add_cp.dropdown_click_input_click(add_cp.cargo_place_owner_select, "Собственное Задание Экспедитора")
    add_cp.click_button(add_cp.child_cp_select, wait="lst")

    cp_list.move_and_click(move_to=cp_list.date_hover, click_to=cp_list.date_clear_button, wait="lst")
    cp_list.click_button(cp_list.cp_list_checkbox_2)
    cp_list.click_button(cp_list.confirm_button)

    add_cp.dropdown_click_input_click(add_cp.lke_cp_type_select, "Короб")
    add_cp.backspace_and_input(add_cp.cp_weight_input, base.random_value_int_str(10, 20000))
    add_cp.backspace_and_input(add_cp.cp_value_input, base.random_value_float_str(0.1, 35.0))
    add_cp.backspace_and_input(add_cp.cp_cost_input, base.random_value_int_str(100, 1000000))
    add_cp.dropdown_click_input_click(add_cp.lke_cp_status_select, "Новое")
    add_cp.dropdown_click_input_enter(add_cp.departure_address_select, "Auto LKE")
    add_cp.dropdown_click_input_enter(add_cp.delivery_address_select, "Auto LKE")
    add_cp.click_button(add_cp.create_cargo_place_button, do_assert=True)
    add_cp.click_button(add_cp.confirm_add_button, wait="lst")

    sidebar.finish_test()
