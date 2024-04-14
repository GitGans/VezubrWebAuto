import allure
from tests.base_test import base_test_with_login
from pages.tariff_luo_add_page import LUOTariffAdd
from pages.tariffs_list_page import TariffsList


@allure.feature('Создание тарифов')
@allure.description('ЛКП. Тест создания ПРР тарифа: название - ПРР-timestamp, спец. - Грузчик, '
                    'минималка/доплата/МКАД - Рандом')
def test_luo_tariff_add_lkp(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkp')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.click_button(tariff_list.add_tariff_button, wait="form")

    add_tariff = LUOTariffAdd(base.driver)
    add_tariff.dropdown_click_input_click(add_tariff.tariff_type_select, "ПРР")
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ПРР-{base.get_timestamp()}")
    add_tariff.dropdown_click_input_click(add_tariff.loader_type_select, "Грузчик")
    add_tariff.click_button(add_tariff.price_input)
    add_tariff.input_in_field(add_tariff.params_input, base.random_value_int_str(2500, 4000))
    add_tariff.click_button(add_tariff.price_hour_input)
    add_tariff.input_in_field(add_tariff.params_input, base.random_value_int_str(500, 1000))
    add_tariff.click_button(add_tariff.price_mrr_input)
    add_tariff.input_in_field(add_tariff.params_input, base.random_value_int_str(100, 500))
    add_tariff.click_button(add_tariff.add_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_add_button, wait="lst")

    sidebar.finish_test()
