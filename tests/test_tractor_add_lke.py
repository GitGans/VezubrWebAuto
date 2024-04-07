import allure
from tests.base_test import base_test
from pages.transport_add_page import TransportAdd
from pages.transports_list_page import TransportsList


@allure.feature('Создание транспортных средств')
@allure.description('ЛКЭ. Тест создания тягача Экс: номер - ТЯГ-timestamp, модель - Тягач, выпуск - 2023г, '
                    'собственник - Подрядчик')
def test_tractor_add_lke(domain):
    base, sidebar = base_test(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                                do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    transports_list.click_button(transports_list.add_transport_button, wait="form")

    add_ts = TransportAdd(base.driver)
    add_ts.dropdown_click_input_click(add_ts.vehicle_type_select, "Тягач")
    add_ts.input_in_field(add_ts.plate_number_input, f"ТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_click_input_click(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_click_input_click(add_ts.year_select, "2023")
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_add_button, wait="lst")

    sidebar.finish_test()
