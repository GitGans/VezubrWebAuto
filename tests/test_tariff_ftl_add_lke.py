import allure
from tests.base_test import base_test_with_login
from pages.tariff_ftl_add_page import FTLTariffAdd
from pages.tariffs_list_page import TariffsList


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЭ. Тест создания FTL тарифа: тип - Почасовой, округление - Час, название - ПЧ-timestamp, '
                    'ТС - 0.5т, кузов - Закрытый, минималка - Рандом')
def test_ftl_hh_tariff_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.click_button(tariff_list.add_tariff_button, wait="form")

    add_tariff = FTLTariffAdd(base.driver)
    add_tariff.dropdown_click_input_click(add_tariff.tariff_type_select, "FTL")
    add_tariff.dropdown_click_input_click(add_tariff.ftl_type_select, "Почасовой")
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ПЧ-{base.get_timestamp()}")
    add_tariff.dropdown_click_input_click(add_tariff.vehicle_type_select, "до 0.5т")
    add_tariff.click_button(add_tariff.body_type_closed_checkbox)
    add_tariff.click_button(add_tariff.price_input)
    add_tariff.input_in_field(add_tariff.hourly_params_input, base.random_value_int_str(3000, 5000))
    add_tariff.click_button(add_tariff.add_hourly_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_button, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЭ. Тест создания FTL тарифа: тип - Фиксированный, маршрут - Екб-Уфа, название - ГГ-timestamp, '
                    'ТС - 1.5т/9м3/4п, кузов - Закрытый, минималка/доп.адрес/ожидание - Рандом')
def test_ftl_cc_tariff_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.click_button(tariff_list.add_tariff_button, wait="form")

    add_tariff = FTLTariffAdd(base.driver)
    add_tariff.dropdown_click_input_click(add_tariff.tariff_type_select, "FTL")
    add_tariff.dropdown_click_input_click(add_tariff.ftl_type_select, "Фиксированный")
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ГГ-{base.get_timestamp()}")
    add_tariff.dropdown_click_input_click(add_tariff.fixed_type_select, "Нас. пункт - Нас. пункт")
    add_tariff.dropdown_click_input_wait_enter(add_tariff.departures_city_input, "г Екатеринбург")
    add_tariff.dropdown_click_input_wait_enter(add_tariff.arrival_city_input, "г Уфа")
    add_tariff.dropdown_click_input_click(add_tariff.vehicle_type_select, "1.5т / 9м3 / 4пал.")
    add_tariff.click_button(add_tariff.body_type_closed_checkbox)
    add_tariff.click_button(add_tariff.price_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_int_str(5000, 10000))
    add_tariff.click_button(add_tariff.address_cost_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_int_str(1000, 3000))
    add_tariff.click_button(add_tariff.free_downtime_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_int_str(10, 60))
    add_tariff.click_button(add_tariff.add_fm_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_button, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЭ. Тест создания FTL тарифа: тип - Пробег, маршрут - Екб-Члб, название - ПБ-timestamp, '
                    'ТС - 5т/36м3/15п, кузов - Закрытый, минималка/доп.адрес/ожидание - Рандом')
def test_ftl_ml_tariff_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.click_button(tariff_list.add_tariff_button, wait="form")

    add_tariff = FTLTariffAdd(base.driver)
    add_tariff.dropdown_click_input_click(add_tariff.tariff_type_select, "FTL")
    add_tariff.dropdown_click_input_click(add_tariff.ftl_type_select, "Пробег")
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ПБ-{base.get_timestamp()}")
    add_tariff.dropdown_click_input_click(add_tariff.vehicle_type_select, "5т / 36м3 / 15пал.")
    add_tariff.click_button(add_tariff.body_type_closed_checkbox)
    add_tariff.click_button(add_tariff.extra_mileage_input)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_int_str(10, 50))
    add_tariff.click_button(add_tariff.address_cost_input)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_int_str(1000, 3000))
    add_tariff.click_button(add_tariff.free_downtime_input)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_int_str(10, 60))
    add_tariff.click_button(add_tariff.add_min_price_button)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_int_str(2500, 10000))
    add_tariff.click_button(add_tariff.add_confirm_button)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_int_str(10, 30))
    add_tariff.input_in_field(add_tariff.mileage_params_input_2, base.random_value_int_str(1, 5))
    add_tariff.input_in_field(add_tariff.mileage_params_input_3, base.random_value_int_str(10, 60))
    add_tariff.click_button(add_tariff.add_fm_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_button, wait="lst")

    sidebar.finish_test()
