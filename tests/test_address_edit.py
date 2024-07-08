import allure
from tests.base_test import base_test_with_login
from pages.address_add_page import AddressAdd
from pages.address_list_page import AddressesList


@allure.story("Critical path test")
@allure.feature('Создание и удаления адресов')
@allure.description('ЛКЭ. Тест создания адреса: статус - Активный, заполняем поля - Все, в конце - Удаляем')
def test_address_edit_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
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
    add_address.dropdown_click_input_wait_enter(
        add_address.address_input,
        f"г Екатеринбург, пр-кт Ленина, д {base.random_value_float_str(1, 150)}",
        wait_presence=True
    )
    # Ввод ИНН владельца адреса и выбор из выпадающего списка
    add_address.dropdown_click_input_wait_enter(add_address.owner_inn_input, "77", wait_presence=True)
    # Ввод id адреса партнера
    add_address.input_in_field(add_address.external_id_input, address_stamp)
    # Ввод требовании к ТС на адресе
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
    # add_address.input_in_field(add_address.additional_first_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    add_address.input_in_field(add_address.email_input, f"E{base.get_timestamp()}@mail.ru")
    add_address.input_in_field(add_address.work_phone_input, base.random_value_float_str(1000000000, 9999999999),
                               click_first=True)
    # add_address.input_in_field(add_address.additional_second_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    # Клик по кнопке создания адреса
    add_address.click_button(add_address.create_address_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_address.click_button(add_address.confirm_button, wait="lst")
    
    # Сброс фильтров и поиск созданного адреса
    address_list.click_button(address_list.reset_button, wait="lst")
    address_list.input_in_field(address_list.name_filter, address_stamp, wait="lst")
    address_list.click_button(address_list.first_address_link, wait="form")
    
    # Редактирование созданного адреса
    add_address.click_button(add_address.edit_button)
    # Генерация нового идентификатора для адреса
    edit_stamp = f"Адрес-{add_address.get_timestamp()}"
    # Редактирование названия адреса
    add_address.backspace_all_and_input(add_address.name_address_input, edit_stamp)
    # Редактирование типа адреса
    add_address.dropdown_click_input_click(add_address.address_type_select, "Торговая точка")
    # Редактирование настройки статусов адреса в МП
    add_address.dropdown_click_input_click(add_address.address_status_in_app, "Укороченный список")
    # Установка статуса адреса в "Не активный"
    add_address.click_button(add_address.address_status_toggl)
    # Редактирование фактического адреса и выбор из выпадающего списка
    add_address.backspace_all_and_input(add_address.address_input, "")
    add_address.dropdown_click_input_wait_enter(
        add_address.address_input,
        f"г Екатеринбург, пр-кт Ленина, д {base.random_value_float_str(1, 150)}",
        wait_presence=True
    )
    # Редактирование ИНН владельца адреса и выбор из выпадающего списка
    add_address.backspace_all_and_input(add_address.owner_inn_input, "")
    add_address.dropdown_click_input_wait_enter(add_address.owner_inn_input, "77", wait_presence=True)
    # Редактирование id адреса партнера
    add_address.backspace_all_and_input(add_address.external_id_input, address_stamp)
    # Редактирование требовании к ТС на адресе
    add_address.backspace_all_and_input(add_address.max_height_input,
                                        base.random_value_float_str(2.0, 5.0, precision=1))
    add_address.backspace_all_and_input(add_address.max_capacity_input, base.random_value_float_str(1000, 5000))
    add_address.dropdown_click_input_click(add_address.loading_type_select, "Боковая")
    add_address.click_button(add_address.entry_pass_toggl)
    add_address.backspace_all_and_input(add_address.time_departure_input, base.random_value_float_str(10, 60))
    add_address.backspace_all_and_input(add_address.time_arrival_input, base.random_value_float_str(10, 60))
    # Редактирование комментария к адресу
    add_address.backspace_all_and_input(add_address.comment_input, "Адрес отредактирован автотестом")
    add_address.click_button(add_address.contacts_tab)
    # Редактирование контактной информации владельца адреса
    add_address.backspace_all_and_input(add_address.edit_contact_person_input, "Другой Василий")
    add_address.backspace_all_and_input(add_address.edit_mobile_phone_input,
                                        base.random_value_float_str(1000000000, 9999999999), click_first=True)
    # add_address.backspace_all_and_input(add_address.edit_additional_first_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    add_address.backspace_all_and_input(add_address.edit_email_input, f"E{base.get_timestamp()}@mail.ru")
    add_address.backspace_all_and_input(add_address.edit_work_phone_input,
                                        base.random_value_float_str(1000000000, 9999999999), click_first=True)
    # add_address.backspace_all_and_input(add_address.edit_additional_second_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    add_address.click_button(add_address.schedule_tab)
    add_address.click_button(add_address.history_tab)
    add_address.click_button(add_address.general_tab)
    # Клик по кнопке сохранения адреса
    add_address.click_button(add_address.create_address_button)
    add_address.flexible_assert_word(add_address.name_address_input, edit_stamp)
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Создание адресов и редактирование')
@allure.description('ЛКЭ. Тест создания адреса: статус - Активный, заполняем поля - Все, редактируем поля - Все')
def test_address_edit_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
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
    add_address.dropdown_click_input_wait_enter(
        add_address.address_input,
        f"г Екатеринбург, пр-кт Ленина, д {base.random_value_float_str(1, 150)}",
        wait_presence=True
    )
    # Ввод ИНН владельца адреса и выбор из выпадающего списка
    add_address.dropdown_click_input_wait_enter(add_address.owner_inn_input, "77", wait_presence=True)
    # Ввод id адреса партнера
    add_address.input_in_field(add_address.external_id_input, address_stamp)
    # Ввод требовании к ТС на адресе
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
    # add_address.input_in_field(add_address.additional_first_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    add_address.input_in_field(add_address.email_input, f"E{base.get_timestamp()}@mail.ru")
    add_address.input_in_field(add_address.work_phone_input, base.random_value_float_str(1000000000, 9999999999),
                               click_first=True)
    # add_address.input_in_field(add_address.additional_second_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    # Клик по кнопке создания адреса
    add_address.click_button(add_address.create_address_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_address.click_button(add_address.confirm_button, wait="lst")
    
    # Сброс фильтров и поиск созданного адреса
    address_list.click_button(address_list.reset_button, wait="lst")
    address_list.input_in_field(address_list.name_filter, address_stamp, wait="lst")
    address_list.click_button(address_list.first_address_link, wait="form")
    
    # Редактирование созданного адреса
    add_address.click_button(add_address.edit_button)
    # Генерация нового идентификатора для адреса
    edit_stamp = f"Адрес-{add_address.get_timestamp()}"
    # Редактирование названия адреса
    add_address.backspace_all_and_input(add_address.name_address_input, edit_stamp)
    # Редактирование типа адреса
    add_address.dropdown_click_input_click(add_address.address_type_select, "Торговая точка")
    # Редактирование настройки статусов адреса в МП
    add_address.dropdown_click_input_click(add_address.address_status_in_app, "Укороченный список")
    # Установка статуса адреса в "Не активный"
    add_address.click_button(add_address.address_status_toggl)
    # Редактирование фактического адреса и выбор из выпадающего списка
    add_address.backspace_all_and_input(add_address.address_input, "")
    add_address.dropdown_click_input_wait_enter(
        add_address.address_input,
        f"г Екатеринбург, пр-кт Ленина, д {base.random_value_float_str(1, 150)}",
        wait_presence=True
    )
    # Редактирование ИНН владельца адреса и выбор из выпадающего списка
    add_address.backspace_all_and_input(add_address.owner_inn_input, "")
    add_address.dropdown_click_input_wait_enter(add_address.owner_inn_input, "77", wait_presence=True)
    # Редактирование id адреса партнера
    add_address.backspace_all_and_input(add_address.external_id_input, address_stamp)
    # Редактирование требовании к ТС на адресе
    add_address.backspace_all_and_input(add_address.max_height_input,
                                        base.random_value_float_str(2.0, 5.0, precision=1))
    add_address.backspace_all_and_input(add_address.max_capacity_input, base.random_value_float_str(1000, 5000))
    add_address.dropdown_click_input_click(add_address.loading_type_select, "Боковая")
    add_address.click_button(add_address.entry_pass_toggl)
    add_address.backspace_all_and_input(add_address.time_departure_input, base.random_value_float_str(10, 60))
    add_address.backspace_all_and_input(add_address.time_arrival_input, base.random_value_float_str(10, 60))
    # Редактирование комментария к адресу
    add_address.backspace_all_and_input(add_address.comment_input, "Адрес отредактирован автотестом")
    add_address.click_button(add_address.contacts_tab)
    # Редактирование контактной информации владельца адреса
    add_address.backspace_all_and_input(add_address.edit_contact_person_input, "Другой Василий")
    add_address.backspace_all_and_input(add_address.edit_mobile_phone_input,
                                        base.random_value_float_str(1000000000, 9999999999), click_first=True)
    # add_address.backspace_all_and_input(add_address.edit_additional_first_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    add_address.backspace_all_and_input(add_address.edit_email_input, f"E{base.get_timestamp()}@mail.ru")
    add_address.backspace_all_and_input(add_address.edit_work_phone_input,
                                        base.random_value_float_str(1000000000, 9999999999), click_first=True)
    # add_address.backspace_all_and_input(add_address.edit_additional_second_input, base.random_value_float_str(1, 999999),
    #                            click_first=True)
    add_address.click_button(add_address.schedule_tab)
    add_address.click_button(add_address.history_tab)
    add_address.click_button(add_address.general_tab)
    # Клик по кнопке сохранения адреса
    add_address.click_button(add_address.create_address_button)
    add_address.flexible_assert_word(add_address.name_address_input, edit_stamp)
    
    # Завершение теста
    sidebar.test_finish()
    