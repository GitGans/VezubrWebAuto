import allure
import pytest
from pages.producers_list_page import ProducersList
from pages.transport_add_page import TransportAdd
from pages.transports_list_page import TransportsList


@allure.story("Smoke test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКЭ. Тест создания и редактирования ТС внутр ПВ: '
                    '1) создаем ТС: номер - ВТС-timestamp, модель - Монорамник, выпуск - 2023г, собственник - '
                    'Подрядчик, тип - Грузопасс, кузов - Металлический, грузоподемность/высота/чел - Мин., '
                    'доп.парам - Нет'
                    '2) редактируем ТС: тип - Грузовая + Манипуль, кузов - Бортовой, грузоподемность/палеты/'
                    'высота - Макс, доп.парам - Все')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_transport_inner_edit_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Монорамное ТС")
    # Выбор владельца транспортного средства
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Выбор первого перевозчика в списке
    producer_list.click_button(producer_list.first_radio_button, wait_type="located")
    producer_list.click_button(producer_list.confirm_choice_button)
    
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ВТС-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Монорамник")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузопассажирская")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, "1")
    add_ts.input_in_field(add_ts.height_from_ground_input, "1")
    add_ts.dropdown_without_input(add_ts.number_passengers_select, "4")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузопассажирская")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Манипулятор")
    add_ts.backspace_and_input(add_ts.capacity_input, "30")
    add_ts.backspace_and_input(add_ts.height_from_ground_input, "4")
    add_ts.input_in_field(add_ts.pallets_input, "35")
    add_ts.input_in_field(add_ts.crane_capacity_input, "10")
    add_ts.input_in_field(add_ts.crane_length_input, "15")
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.click_button(add_ts.sanitary_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.dropdown_without_input(add_ts.first_pass_type_select, "МКАД", index=1)
    add_ts.click_button(add_ts.first_pass_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.dropdown_without_input(add_ts.second_pass_type_select, "СК", index=2)
    add_ts.click_button(add_ts.second_pass_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.dropdown_without_input(add_ts.third_pass_type_select, "ТТК", index=3)
    add_ts.click_button(add_ts.third_pass_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.click_button(add_ts.gps_monitoring_toggl)
    add_ts.all_additional_params_without_gps()
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКЭ. Тест создания и редактирования ПП внутр ПВ: '
                    '1) создаем ПП: номер - ВПП-timestamp, модель - Полуприцеп, выпуск - 2023г, собственник - '
                    'Подрядчик, тип - Грузовая, кузов - Тентованный, грузоподемность/объем/паллет/высота - Макс., '
                    'доп.парам - Все'
                    '2) редактируем ПП: тип - Грузовая, кузов - Фургон, грузоподемность/объем/паллет/высота - Мин, '
                    'доп.парам - Нет')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_semitrailer_inner_edit_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Полуприцеп")
    # Выбор владельца транспортного средства
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Выбор первого перевозчика в списке
    producer_list.click_button(producer_list.first_radio_button, wait_type="located")
    producer_list.click_button(producer_list.confirm_choice_button)
    
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ВПП-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Полуприцеп")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Тентованный")
    add_ts.input_in_field(add_ts.capacity_input, "100")
    add_ts.input_in_field(add_ts.volume_input, "120")
    add_ts.input_in_field(add_ts.pallets_input, "35")
    add_ts.input_in_field(add_ts.height_from_ground_input, "5")
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.click_button(add_ts.sanitary_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.all_additional_params_without_gps()
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.backspace_and_input(add_ts.capacity_input, "0.5")
    add_ts.backspace_and_input(add_ts.volume_input, "0.5")
    add_ts.backspace_and_input(add_ts.pallets_input, "0")
    add_ts.backspace_and_input(add_ts.height_from_ground_input, "5")
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.all_additional_params_without_gps()
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    # Сохранение внесенных изменений транспортного средства
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКЭ. Тест создания и редактирования ПП Экс: '
                    '1) создаем ПП: номер - ПП-timestamp, модель - Полуприцеп, выпуск - 2020г, собственник - Аренда,'
                    'тип - Цистерна, кузов - Цистерна, грузоподемность/объем/высота/отсеков - Мин. доп.парам - Нет'
                    '2) редактируем ПП: тип - Автовоз, кузов - Автовоз, грузоподемность/высота/машин - Макс, '
                    'доп.парам - Все')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_semitrailer_edit_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Полуприцеп")
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ПП-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Полуприцеп")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Подрядчик является собственником")
    add_ts.dropdown_without_input(add_ts.year_select, "2020")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Цистерна")
    add_ts.input_in_field(add_ts.capacity_input, "10")
    add_ts.input_in_field(add_ts.volume_input, "20")
    add_ts.input_in_field(add_ts.height_from_ground_input, "1")
    add_ts.input_in_field(add_ts.compartment_count_input, "1")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Аренда")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Автовоз")
    add_ts.backspace_and_input(add_ts.capacity_input, "40")
    add_ts.backspace_and_input(add_ts.height_from_ground_input, "5")
    add_ts.input_in_field(add_ts.car_count_input, "10")
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.click_button(add_ts.sanitary_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.click_button(add_ts.covered_body_toggl)
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    add_ts.all_additional_params_without_gps()
    # Сохранение внесенных изменений транспортного средства
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКЭ. Тест создания и редактирования Тягача внутр. ПВ Экс: '
                    '1) создаем Тяг: номер - ВТЯГ-timestamp, модель - Тягач, выпуск - 2019г, собственник - Аренда,'
                    'доп.парам - Все'
                    '2) редактируем Тяг: выпуск - 2021г, собственник - Лизинг, доп.парам - Нет')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tractor_inner_edit_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку транспортных средств
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    
    transports_list = TransportsList(base.driver)
    # Клик по кнопке добавления транспортного средства
    transports_list.click_button(transports_list.add_transport_button)
    
    add_ts = TransportAdd(base.driver)
    # Выбор типа транспортного средства
    add_ts.dropdown_without_input(add_ts.vehicle_type_select, "Тягач")
    # Выбор владельца транспортного средства
    add_ts.click_button(add_ts.vehicle_owner_select, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Выбор первого перевозчика в списке
    producer_list.click_button(producer_list.first_radio_button, wait_type="located")
    producer_list.click_button(producer_list.confirm_choice_button)
    
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ВТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Аренда")
    add_ts.dropdown_without_input(add_ts.year_select, "2019")
    add_ts.dropdown_without_input(add_ts.first_pass_type_select, "МКАД", index=1)
    add_ts.click_button(add_ts.tractor_first_pass_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.dropdown_without_input(add_ts.second_pass_type_select, "СК", index=2)
    add_ts.click_button(add_ts.tractor_second_pass_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.dropdown_without_input(add_ts.third_pass_type_select, "ТТК", index=3)
    add_ts.click_button(add_ts.tractor_third_pass_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.click_button(add_ts.gps_monitoring_toggl)
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_without_input(add_ts.year_select, "2021")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Лизинг")
    add_ts.move_and_click(move_to=add_ts.third_pass_type_select, click_to=add_ts.close_circle_button, click_index=9)
    add_ts.move_and_click(move_to=add_ts.second_pass_type_select, click_to=add_ts.close_circle_button, click_index=7)
    add_ts.move_and_click(move_to=add_ts.first_pass_type_select, click_to=add_ts.close_circle_button, click_index=5)
    add_ts.click_button(add_ts.gps_monitoring_toggl)
    # Сохранение внесенных изменений транспортного средства
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста
