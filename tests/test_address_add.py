import allure
import pytest
from pages.address_add_page import AddressAdd
from pages.address_list_page import AddressesList


@allure.story("Smoke test")
@allure.feature('Создание и удаления адресов')
@allure.description('ЛКЭ. Тест создания адреса: статус - Активный, заполняем поля - Все, в конце - Удаляем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_address_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    
    address_list = AddressesList(base.driver)
    # Клик по кнопке добавления адреса
    address_list.click_button(address_list.add_address_button)
    
    add_address = AddressAdd(base.driver)
    # Генерация уникального идентификатора для адреса
    address_stamp = f"Адрес-{add_address.get_timestamp()}"
    # Ввод названия адреса
    add_address.input_in_field(add_address.name_address_input, address_stamp)
    # Выбор типа адреса
    add_address.dropdown_click_input_click(add_address.address_type_select, "Склад")
    # Настройка статусов адреса в МП
    add_address.dropdown_click_input_click(add_address.address_status_in_app, "Полный список")
    # Установка статуса адреса в "Активный"
    add_address.click_button(add_address.address_status_toggl)
    # Ввод фактического адреса и выбор из выпадающего списка
    add_address.dropdown_with_input(
        add_address.address_input,
        f"г Екатеринбург, пр-кт Ленина, д {base.random_value_float_str(1, 150)}",
        wait_presence=True
    )
    # Ввод ИНН владельца адреса и выбор из выпадающего списка
    add_address.dropdown_with_input(add_address.owner_inn_input, "77", wait_presence=True)
    # Ввод id адреса партнера
    add_address.input_in_field(add_address.external_id_input, address_stamp)
    # Ввод требований к ТС на адресе
    add_address.input_in_field(add_address.max_height_input, base.random_value_float_str(2.0, 5.0, precision=1))
    add_address.input_in_field(add_address.max_capacity_input, base.random_value_float_str(1000, 5000))
    add_address.dropdown_click_input_click(add_address.loading_type_select, "Верхняя")
    add_address.click_button(add_address.entry_pass_toggl)
    add_address.input_in_field(add_address.time_departure_input, base.random_value_float_str(10, 60))
    add_address.input_in_field(add_address.time_arrival_input, base.random_value_float_str(10, 60))
    # Ввод комментария к адресу
    add_address.input_in_field(add_address.comment_input, "Адрес создан автотестом")
    # Ввод контактной информации владельца адреса
    add_address.input_in_field(add_address.contact_person_input, "Какой-то Василий")
    add_address.input_in_field(add_address.mobile_phone_input, base.random_value_float_str(1000000000, 9999999999),
                               click_first=True)
    add_address.input_in_field(add_address.additional_first_input, base.random_value_float_str(1, 999999),
                               click_first=True)
    add_address.input_in_field(add_address.email_input, f"E{base.get_timestamp()}@mail.ru")
    add_address.input_in_field(add_address.work_phone_input, base.random_value_float_str(1000000000, 9999999999),
                               click_first=True)
    add_address.input_in_field(add_address.additional_second_input, base.random_value_float_str(1, 999999),
                               click_first=True)
    # Клик по кнопке создания адреса
    add_address.click_button(add_address.create_address_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_address.click_button(add_address.confirm_button, wait="lst")
    
    # Сброс фильтров и поиск созданного адреса
    address_list.click_button(address_list.reset_button, wait="lst")
    address_list.input_in_field(address_list.name_filter, address_stamp, wait="lst")
    address_list.click_button(address_list.first_address_link, wait="form")
    
    # Удаление созданного адреса
    add_address.click_button(add_address.delete_button, do_assert=True)
    add_address.click_button(add_address.confirm_button, wait="lst")
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и удаления адресов')
@allure.description('ЛКЭ. Тест создания адреса: статус - Активный, заполняем поля - Все, в конце - Удаляем')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_address_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    
    address_list = AddressesList(base.driver)
    # Клик по кнопке добавления адреса
    address_list.click_button(address_list.add_address_button)
    
    add_address = AddressAdd(base.driver)
    # Генерация уникального идентификатора для адреса
    address_stamp = f"Адрес-{add_address.get_timestamp()}"
    # Ввод названия адреса
    add_address.input_in_field(add_address.name_address_input, address_stamp)
    # Выбор типа адреса
    add_address.dropdown_click_input_click(add_address.address_type_select, "Склад")
    # Настройка статусов адреса в МП
    add_address.dropdown_click_input_click(add_address.address_status_in_app, "Полный список")
    # Установка статуса адреса в "Активный"
    add_address.click_button(add_address.address_status_toggl)
    # Ввод фактического адреса и выбор из выпадающего списка
    add_address.dropdown_with_input(
        add_address.address_input,
        f"г Екатеринбург, пр-кт Ленина, д {base.random_value_float_str(1, 150)}",
        wait_presence=True
    )
    # Ввод ИНН владельца адреса и выбор из выпадающего списка
    add_address.dropdown_with_input(add_address.owner_inn_input, "77", wait_presence=True)
    # Ввод id адреса партнера
    add_address.input_in_field(add_address.external_id_input, address_stamp)
    # Ввод требований к ТС на адресе
    add_address.input_in_field(add_address.max_height_input, base.random_value_float_str(2.0, 5.0, precision=1))
    add_address.input_in_field(add_address.max_capacity_input, base.random_value_float_str(1000, 5000))
    add_address.dropdown_click_input_click(add_address.loading_type_select, "Верхняя")
    add_address.click_button(add_address.entry_pass_toggl)
    add_address.input_in_field(add_address.time_departure_input, base.random_value_float_str(10, 60))
    add_address.input_in_field(add_address.time_arrival_input, base.random_value_float_str(10, 60))
    # Ввод комментария к адресу
    add_address.input_in_field(add_address.comment_input, "Адрес создан автотестом")
    # Ввод контактной информации владельца адреса
    add_address.input_in_field(add_address.contact_person_input, "Какой-то Василий")
    add_address.input_in_field(add_address.mobile_phone_input, base.random_value_float_str(1000000000, 9999999999),
                               click_first=True)
    add_address.input_in_field(add_address.additional_first_input, base.random_value_float_str(1, 999999),
                               click_first=True)
    add_address.input_in_field(add_address.email_input, f"E{base.get_timestamp()}@mail.ru")
    add_address.input_in_field(add_address.work_phone_input, base.random_value_float_str(1000000000, 9999999999),
                               click_first=True)
    add_address.input_in_field(add_address.additional_second_input, base.random_value_float_str(1, 999999),
                               click_first=True)
    # Клик по кнопке создания адреса
    add_address.click_button(add_address.create_address_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_address.click_button(add_address.confirm_button, wait="lst")
    
    # Сброс фильтров и поиск созданного адреса
    address_list.click_button(address_list.reset_button, wait="lst")
    address_list.input_in_field(address_list.name_filter, address_stamp, wait="lst")
    address_list.click_button(address_list.first_address_link, wait="form")
    
    # Удаление созданного адреса
    add_address.click_button(add_address.delete_button, do_assert=True)
    add_address.click_button(add_address.confirm_button, wait="lst")
    # Конец теста
    