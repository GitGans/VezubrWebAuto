import allure
from tests.base_test import base_test_with_login
from pages.tariff_ltl_add_page import LTLTariffAdd
from pages.tariffs_list_page import TariffsList


@allure.story("Critical path test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЗ. Тест создания LTL тарифа: название - LTL-timestamp, тип - Короб, мин.вес/объем вес/сбор '
                    'прям./сбор обр. - Рандом, регион - Свердл/Алтай, минималка/доплата/темп.коэф/срок - Рандом')
def test_ltl_tariff_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.click_button(tariff_list.add_tariff_button)

    add_tariff = LTLTariffAdd(base.driver)
    add_tariff.dropdown_click_input_click(add_tariff.tariff_type_select, "LTL")
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"LTL-{base.get_timestamp()}")
    add_tariff.dropdown_click_input_click(add_tariff.ltl_type_select, "Короб")
    add_tariff.backspace_len_and_input(add_tariff.min_weight_input, base.random_value_float_str(10, 100))
    add_tariff.backspace_len_and_input(add_tariff.volumetric_weight_input, base.random_value_float_str(10, 100))
    add_tariff.backspace_len_and_input(add_tariff.direct_price_input, base.random_value_float_str(100, 500))
    add_tariff.backspace_len_and_input(add_tariff.reverse_price_input, base.random_value_float_str(100, 500))
    add_tariff.dropdown_click_input_wait_enter(add_tariff.dispatch_region_select, "Свердловская область")
    add_tariff.dropdown_click_input_wait_enter(add_tariff.delivery_region_select, "Алтайский край")
    add_tariff.input_in_field(add_tariff.min_price_input, base.random_value_float_str(1000, 3000))
    add_tariff.input_in_field(add_tariff.kg_price_input, base.random_value_float_str(50, 200))
    add_tariff.input_in_field(add_tariff.temp_coeff_input, base.random_value_float_str(1.0, 5.0))
    add_tariff.input_in_field(add_tariff.delivery_time_input, base.random_value_float_str(5, 50))
    add_tariff.click_button(add_tariff.add_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_add_button, wait="lst")

    sidebar.test_finish()
