import allure
from tests.base_test import base_test_with_login
from pages.transport_add_page import TransportAdd
from pages.transports_list_page import TransportsList


@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКЭ. Тест создания и редактирования ТС внутр ПВ: '
                    '1) создаем ТС: номер - ТС-timestamp, модель - Монорамник, выпуск - 2023г, собственник - Подрядчик,'
                    'тип - Грузопасс, кузов - Металлический, грузоподемность/высота - Мин. доп.парам - Нет'
                    '2) редактируем ТС: тип - Грузовая + Манипуль, кузов - Бортовой, грузоподемность/палеты/'
                    'высота - Макс, доп.парам - Все')
def test_transport_inner_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                                do_assert=True, wait="lst")

    transports_list = TransportsList(base.driver)
    transports_list.click_button(transports_list.add_transport_button, wait="form")

    add_ts = TransportAdd(base.driver)
    add_ts.dropdown_click_input_click(add_ts.vehicle_type_select, "Монорамное ТС")
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")

    transports_list.click_button_located(transports_list.first_radio_button)
    transports_list.click_button(transports_list.confirm_choice_button)

    plate_number = f"ТС{base.get_timestamp()}"
    add_ts.input_in_field(add_ts.plate_number_input, plate_number)
    add_ts.input_in_field(add_ts.mark_model_input, "Монорамник")
    add_ts.dropdown_click_input_click(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_click_input_click(add_ts.year_select, "2022")
    add_ts.dropdown_click_input_click(add_ts.vehicle_categories_select, "Грузопассажирская")
    add_ts.dropdown_click_input_click(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, "1.0")
    add_ts.input_in_field(add_ts.height_from_ground_input, "1.0")
    add_ts.dropdown_click_input_click(add_ts.number_passengers_select, "4")
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_add_button, wait="form")

    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_click_input_click(add_ts.vehicle_categories_select, "Грузопассажирская")
    add_ts.dropdown_click_input_click(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_click_input_click(add_ts.vehicle_categories_select, "Манипулятор")
    add_ts.backspace_and_input(add_ts.capacity_input, "30.0")
    add_ts.backspace_and_input(add_ts.height_from_ground_input, "4.0")
    add_ts.input_in_field(add_ts.pallets_input, "35.0")
    add_ts.input_in_field(add_ts.crane_capacity_input, "10.0")
    add_ts.input_in_field(add_ts.crane_length_input, "15")
    add_ts.click_button(add_ts.hydro_lift_toggl)
    add_ts.click_button(add_ts.gps_monitoring_toggl)
    add_ts.click_button(add_ts.pallets_jack_toggl)
    add_ts.click_button(add_ts.conics_toggl)
    add_ts.click_button(add_ts.strap_toggl)
    add_ts.click_button(add_ts.chain_toggl)
    add_ts.click_button(add_ts.tarpaulin_toggl)
    add_ts.click_button(add_ts.net_toggl)
    add_ts.click_button(add_ts.wheel_chock_toggl)
    add_ts.click_button(add_ts.corner_pillar_toggl)
    add_ts.click_button(add_ts.doppel_stock_toggl)
    add_ts.click_button(add_ts.wooden_floor_toggl)
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    # Добавить пропуска
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True, wait="form")

    sidebar.finish_test()
