import allure
from tests.base_test import base_test
from pages.transport_add_page import TransportAdd
from pages.transports_list_page import TransportsList


@allure.feature('Создание транспортных средств')
@allure.description('ЛКП. Тест создания ТС: номер - ТС-timestamp, модель - Монорамник, выпуск - 2023г, собственник '
                    '- Подрядчик, тип - Грузовой, кузов - Тент, грузоподемность/объем/палеты/высота - Рандом')
def test_transport_add_lkp(domain):
    base, sidebar = base_test(domain=domain, role='lkp')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                                do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    transports_list.click_button(transports_list.add_transport_button, wait="form")

    add_ts = TransportAdd(base.driver)
    add_ts.dropdown_click_input_click(add_ts.vehicle_type_select, "Монорамное ТС")
    add_ts.input_in_field(add_ts.plate_number_input, f"ТС{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Монорамник")
    add_ts.dropdown_click_input_click(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_click_input_click(add_ts.year_select, "2022")
    add_ts.dropdown_click_input_click(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_click_input_click(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, base.random_value_float_str(0.5, 30.0))
    add_ts.input_in_field(add_ts.volume_input, base.random_value_float_str(0.5, 120.0))
    add_ts.input_in_field(add_ts.pallets_input, base.random_value_int_str(0, 35))
    add_ts.input_in_field(add_ts.height_from_ground_input, base.random_value_float_str(1.0, 4.0))
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_add_button, wait="lst")

    sidebar.finish_test()
