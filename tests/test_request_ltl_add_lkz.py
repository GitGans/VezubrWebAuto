import time
import allure
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList
from pages.request_ltl_add_page import LTLAdd
from tests.base_test import base_test_with_login


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание LTL заявок')
@allure.description('ЛКЗ. Тест создания LTL заявки: дата - Сейчас +30мин, гм - Первое в списке, публикация - Позже')
def test_ltl_request_no_publish_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    add_cp.add_base_cargo_place()

    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ltl_button,
                           do_assert=True, wait="form")

    ltl = LTLAdd(base.driver)
    ltl.dropdown_click_input_click(ltl.request_type_select, "Доставку ГМ (LTL)")
    ltl.click_button(ltl.attach_cargo_place_button, wait="lst")

    cpl = CargoPlaceList(base.driver)
    cpl.click_button(cpl.cp_list_checkbox, 2)
    cpl.click_button(cpl.confirm_button)

    ltl.add_base_ltl()
    time.sleep(1)
    ltl.click_button(ltl.publish_later_button, do_assert=True, wait="lst")

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание LTL заявок')
@allure.description('ЛКЗ. Тест создания LTL заявки: дата - Сейчас +30мин, гм - Первое в списке, публикация - Ставка, '
                    'стоимость - Рандом')
def test_ltl_request_rate_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    add_cp.add_base_cargo_place()

    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ltl_button,
                           do_assert=True, wait="form")

    ltl = LTLAdd(base.driver)
    ltl.dropdown_click_input_click(ltl.request_type_select, "Доставку ГМ (LTL)")
    ltl.click_button(ltl.attach_cargo_place_button, wait="lst")

    cpl = CargoPlaceList(base.driver)
    cpl.click_button(cpl.cp_list_checkbox, 2)
    cpl.click_button(cpl.confirm_button)

    ltl.add_base_ltl()
    time.sleep(1)
    ltl.click_button(ltl.publish_naw_button, wait="form")
    ltl.click_button(ltl.tariff_button, wait="form")
    time.sleep(1)
    ltl.click_button(ltl.rate_radio)
    ltl.click_button(ltl.producer_select)
    ltl.click_button(ltl.producer_button)
    ltl.input_in_field(ltl.rate_input, base.random_value_float_str(1000, 100000), click_first=True)
    ltl.click_button(ltl.publish_button, do_assert=True)
    ltl.click_button(ltl.ok_button, wait="lst")

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание LTL заявок')
@allure.description('ЛКЗ. Тест создания LTL заявки: дата - Сейчас +30мин, гм - Первое в списке, публикация - Тариф')
def test_ltl_request_tariff_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    add_cp.add_base_cargo_place()

    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ltl_button,
                           do_assert=True, wait="form")

    ltl = LTLAdd(base.driver)
    ltl.dropdown_click_input_click(ltl.request_type_select, "Доставку ГМ (LTL)")
    ltl.click_button(ltl.attach_cargo_place_button, wait="lst")

    cpl = CargoPlaceList(base.driver)
    cpl.click_button(cpl.cp_list_checkbox, 2)
    cpl.click_button(cpl.confirm_button)

    ltl.add_base_ltl()
    time.sleep(1)
    ltl.click_button(ltl.publish_naw_button, wait="form")
    ltl.click_button(ltl.tariff_button, wait="form")
    time.sleep(1)
    ltl.click_button(ltl.producer_select)
    ltl.click_button(ltl.producer_lke_button)
    ltl.click_button(ltl.text_to_click)
    ltl.click_button(ltl.publish_button, do_assert=True)
    ltl.click_button(ltl.ok_button, wait="lst")

    sidebar.test_finish()
