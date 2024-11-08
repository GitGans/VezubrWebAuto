import allure
import pytest
from pages.transport_add_page import TransportAdd
from pages.transports_list_page import TransportsList


@allure.story("Smoke test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКП. Тест создания и редактирования ТС ПВ: '
                    '1) создаем ТС: номер - ТС-timestamp, модель - Монорамник, выпуск - 2023г, '
                    'собственник - Безвозмездное пользование, тип - Манипулятор, кузов - Бортовой, '
                    'грузоподемность/высота/стрела - Макс. доп.парам - Все'
                    '2) редактируем ТС: тип - Грузовая + Грузопас, кузов - Тентованный, '
                    'грузоподемность/палеты/высота/чел - Мин, доп.парам - Нет')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_transport_edit_lkp(base_fixture, domain):
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
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТС-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Монорамник")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Безвозмездное пользование")
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
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
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Манипулятор")
    add_ts.input_in_field(add_ts.capacity_input, "30")
    add_ts.input_in_field(add_ts.height_from_ground_input, "5")
    add_ts.input_in_field(add_ts.crane_capacity_input, "10")
    add_ts.input_in_field(add_ts.crane_length_input, "15")
    add_ts.click_button(add_ts.gps_monitoring_toggl)
    add_ts.all_additional_params_without_gps()
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")

    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Манипулятор")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузопассажирская")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.move_and_click(move_to=add_ts.third_pass_type_select, click_to=add_ts.close_circle_button, click_index=10)
    add_ts.move_and_click(move_to=add_ts.second_pass_type_select, click_to=add_ts.close_circle_button, click_index=8)
    add_ts.move_and_click(move_to=add_ts.first_pass_type_select, click_to=add_ts.close_circle_button, click_index=6)
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.backspace_and_input(add_ts.capacity_input, "1")
    add_ts.input_in_field(add_ts.pallets_input, "0")
    add_ts.backspace_and_input(add_ts.height_from_ground_input, "1")
    add_ts.dropdown_without_input(add_ts.number_passengers_select, "4")
    add_ts.click_button(add_ts.gps_monitoring_toggl)
    add_ts.all_additional_params_without_gps()
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКП. Тест создания и редактирования ПП ПВ: '
                    '1) создаем ПП: номер - ПП-timestamp, модель - Полуприцеп, выпуск - 2023г, собственник - Подрядчик,'
                    'тип - Грузовая, кузов - Бортовой, грузоподемность/паллет/высота - Мин. доп.парам - Нет'
                    '2) редактируем ПП: тип - Трал, кузов - Трал, выпуск = 2020, собственник - Совместная '
                    'собственность супругов, грузоподемность/высота/площадка - Макс, доп.парам - Все')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_semitrailer1_edit_lkp(base_fixture, domain):
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
    add_ts.dropdown_without_input(add_ts.year_select, "2023")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Грузовая")
    add_ts.dropdown_without_input(add_ts.vehicle_body_types_select, "Бортовой")
    add_ts.input_in_field(add_ts.capacity_input, "0.5")
    add_ts.input_in_field(add_ts.pallets_input, "0")
    add_ts.input_in_field(add_ts.height_from_ground_input, "1")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Совместная собственность супругов")
    add_ts.dropdown_without_input(add_ts.year_select, "2020")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Трал")
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.click_button(add_ts.sanitary_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.backspace_and_input(add_ts.capacity_input, click_first=True, value="80")
    add_ts.backspace_and_input(add_ts.height_from_ground_input, "5")
    add_ts.input_in_field(add_ts.platform_height_input, "1.5")
    add_ts.input_in_field(add_ts.platform_length_input, "35")
    add_ts.all_additional_params_without_gps()
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКП. Тест создания и редактирования ПП ПВ: '
                    '1) создаем ПП: номер - ПП-timestamp, модель - Полуприцеп, выпуск - 2020г, собственник - Аренда,'
                    'тип - Самосвал, кузов - Самосвал, грузоподемность/объем/высота - Макс. доп.парам - Все'
                    '2) редактируем ПП: выпуск - 2024г, собственник - Лизинг, тип - Контейнеровоз, кузов - '
                    'Контейнеровоз, грузоподемность/высота/площадка - Мин, доп.парам - Нет')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_semitrailer2_edit_lkp(base_fixture, domain):
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
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Аренда")
    add_ts.dropdown_without_input(add_ts.year_select, "2020")
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.click_button(add_ts.sanitary_date_button)
    add_ts.input_in_field(add_ts.calendar_input, "10102045")
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Самосвал")
    add_ts.input_in_field(add_ts.capacity_input, "50")
    add_ts.input_in_field(add_ts.volume_input, "40")
    add_ts.input_in_field(add_ts.height_from_ground_input, "5")
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    add_ts.all_additional_params_without_gps()
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")
    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Лизинг")
    add_ts.dropdown_without_input(add_ts.year_select, "2024")
    add_ts.click_button(add_ts.sanitation_toggl)
    add_ts.dropdown_without_input(add_ts.vehicle_categories_select, "Контейнеровоз")
    add_ts.backspace_and_input(add_ts.capacity_input, "25")
    add_ts.backspace_and_input(add_ts.height_from_ground_input, "1")
    add_ts.input_in_field(add_ts.platform_height_input, "1.5")
    add_ts.input_in_field(add_ts.platform_length_input, "6")
    add_ts.click_button(add_ts.side_loading_toggl)
    add_ts.click_button(add_ts.top_loading_toggl)
    add_ts.all_additional_params_without_gps()
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и редактирование транспортных средств')
@allure.description('ЛКП. Тест создания и редактирования Тягача внутр. ПВ: '
                    '1) создаем Тяг: номер - Тяг-timestamp, модель - Тягач, выпуск - 2019г, собственник - Лизинг,'
                    'доп.парам - Нет'
                    '2) редактируем Тяг: выпуск - 2021г, собственник - Аренда, доп.парам - Все')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_tractor_edit_lkp(base_fixture, domain):
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
    # Заполнение данных о транспортном средстве
    add_ts.input_in_field(add_ts.plate_number_input, f"ТЯГ-{base.get_timestamp()}")
    add_ts.input_in_field(add_ts.mark_model_input, "Тягач")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Лизинг")
    add_ts.dropdown_without_input(add_ts.year_select, "2019")
    # Создание транспортного средства
    add_ts.click_button(add_ts.create_vehicle_button, do_assert=True)
    add_ts.click_button(add_ts.confirm_button, wait="form")

    # Редактирование транспортного средства
    add_ts.click_button(add_ts.edit_button)
    add_ts.dropdown_without_input(add_ts.year_select, "2021")
    add_ts.dropdown_without_input(add_ts.owner_types_select, "Аренда")
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
    add_ts.click_button(add_ts.edit_confirm_button, do_assert=True)
    # Конец теста
