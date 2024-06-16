import allure
from tests.base_test import base_test_with_login
from pages.loader_add_page import LoaderAdd
from pages.loader_list_page import LoaderList


@allure.story("Smoke test")
@allure.feature('Создание и редвктирование специалиста')
@allure.description('ЛКЭ. Тест создания  и редвктирование специалиста Экс: '
                    '1) создаем: ФИО - ФИО-timestamp, паспорт - Албания/Тирана, тип - Грузчик/Сборщик/Стропальщик, '
                    'годен до - 10.10.2045, № паспорт/код/права/тлф.апп/тлф. - Рандом.'
                    '2) редактируем: ФИО - ФИО-timestamp, паспорт - РФ, тип - Такелажник/Упаковщик/Карщик, '
                    'годен до - 10.10.2045, № паспорт/код/права/тлф.апп/тлф. - Рандом.')
def test_loader1_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")

    loader_list = LoaderList(base.driver)
    loader_list.click_button(loader_list.add_loader_button, wait="form")

    add_loader = LoaderAdd(base.driver)
    add_loader.click_button(add_loader.passport_toggl)
    add_loader.dropdown_click_input_click(add_loader.loader_country_select, "Албания / Albania / ALB")
    add_loader.input_in_field(add_loader.loader_city_input, "Тирана")
    surname = f"Ф-{add_loader.get_timestamp()}"
    add_loader.input_in_field(add_loader.surname_input, surname)
    add_loader.input_in_field(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.passport_id_input, add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.input_in_field(add_loader.passport_by_input, "Верховный грузила")
    add_loader.input_in_field(add_loader.passport_code_input,
                              add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Грузчик", 2, 1)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Сборщик", 3, 2)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Стропальщик", 4, 3)
    add_loader.click_button(add_loader.date_button, index=3)
    add_loader.input_in_field(add_loader.calendar_input, value="10102045")
    add_loader.input_in_field(add_loader.app_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.contact_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.reg_address_input, "Мой адрес – какой то Другой")
    add_loader.backspace_all_and_input(add_loader.fact_address_input, "Мой адрес – какой то Другой")
    add_loader.click_button(add_loader.create_loader_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="lst")
    
    loader_list.input_in_field(loader_list.surname_filter, value=surname, wait="lst")
    loader_list.click_button(loader_list.first_loader_link, wait="form")
    
    add_loader.click_button(add_loader.loader_edit_button, wait="form")
    add_loader.click_button(add_loader.passport_toggl)
    add_loader.backspace_all_and_input(add_loader.surname_input, f"Ф-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.passport_id_input,
                                       add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.backspace_all_and_input(add_loader.passport_by_input, "Главный грузила")
    add_loader.backspace_all_and_input(add_loader.passport_code_input,
                                       add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=3, click_to=add_loader.close_circle_button, click_index=6)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=2, click_to=add_loader.close_circle_button, click_index=5)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=1, click_to=add_loader.close_circle_button, click_index=4)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Такелажник")
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Упаковщик", 2, 2)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Карщик", 3, 3)
    add_loader.click_button(add_loader.date_button, index=3)
    add_loader.input_in_field(add_loader.calendar_input, value="10102045")
    add_loader.backspace_all_and_input(add_loader.app_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.contact_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.reg_address_input, "Мой адрес – Не дом и не улица")
    add_loader.input_in_field(add_loader.fact_address_input, "Мой адрес – Советский Союз.")
    add_loader.click_button(add_loader.confirm_edit_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="form")
    
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание и редвктирование специалиста')
@allure.description('ЛКЭ. Тест создания  и редвктирование специалиста Экс: '
                    '1) создаем: ФИО - ФИО-timestamp, паспорт - РФ, тип - Грузчик/Упаковщик/Такелажник, '
                    'годен до - 10.10.2045, № паспорт/код/права/тлф.апп/тлф. - Рандом.'
                    '2) редактируем: ФИО - ФИО-timestamp, паспорт - Албания/Тирана, тип - Сборщик/Стропальщик, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом.')
def test_loader2_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    
    loader_list = LoaderList(base.driver)
    loader_list.click_button(loader_list.add_loader_button, wait="form")
    
    add_loader = LoaderAdd(base.driver)
    surname = f"Ф-{add_loader.get_timestamp()}"
    add_loader.input_in_field(add_loader.surname_input, surname)
    add_loader.input_in_field(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.passport_id_input, add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.input_in_field(add_loader.passport_by_input, "Верховный грузила")
    add_loader.input_in_field(add_loader.passport_code_input,
                              add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Грузчик", 1, 1)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Упаковщик", 2, 2)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Такелажник", 3, 3)
    add_loader.input_in_field(add_loader.app_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.contact_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.reg_address_input, "Мой адрес – Не дом и не улица")
    add_loader.input_in_field(add_loader.fact_address_input, "Мой адрес – Советский Союз.")
    add_loader.click_button(add_loader.create_loader_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="lst")
    
    loader_list.input_in_field(loader_list.surname_filter, value=surname, wait="lst")
    loader_list.click_button(loader_list.first_loader_link, wait="form")
    
    add_loader.click_button(add_loader.loader_edit_button, wait="form")
    add_loader.click_button(add_loader.passport_toggl)
    add_loader.dropdown_click_input_click(add_loader.loader_country_select, "Албания / Albania / ALB")
    add_loader.input_in_field(add_loader.loader_city_input, "Тирана")
    add_loader.backspace_all_and_input(add_loader.surname_input, f"Ф-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.passport_id_input,
                                       add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.backspace_all_and_input(add_loader.passport_by_input, "Главный грузила")
    add_loader.backspace_all_and_input(add_loader.passport_code_input,
                                       add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=4, click_to=add_loader.close_circle_button, click_index=6)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=3, click_to=add_loader.close_circle_button, click_index=5)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=2, click_to=add_loader.close_circle_button, click_index=4)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Такелажник", 2, 1)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Упаковщик", 3, 2)
    add_loader.click_button(add_loader.date_button, index=2)
    add_loader.input_in_field(add_loader.calendar_input, value="10102045")
    add_loader.backspace_all_and_input(add_loader.app_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.contact_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.reg_address_input, "Мой адрес – какой то Другой")
    add_loader.backspace_all_and_input(add_loader.fact_address_input, "Мой адрес – какой то Другой")
    add_loader.click_button(add_loader.confirm_edit_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="form")
    
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание и редвктирование специалиста')
@allure.description('ЛКП. Тест создания  и редвктирование специалиста ПВ: '
                    '1) создаем: ФИО - ФИО-timestamp, паспорт - Азербайджан/Баку, тип - Упаковщи/Сборщик/Штабелерщик, '
                    'годен до - 10.10.2045, № паспорт/код/права/тлф.апп/тлф. - Рандом.'
                    '2) редактируем: ФИО - ФИО-timestamp, паспорт - РФ, тип - Грузчик/Такелажник/Стропальщик, '
                    'годен до - 10.10.2045, № паспорт/код/права/тлф.апп/тлф. - Рандом.')
def test_loader1_edit_lkp(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkp')
    
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    
    loader_list = LoaderList(base.driver)
    loader_list.click_button(loader_list.add_loader_button, wait="form")
    
    add_loader = LoaderAdd(base.driver)
    add_loader.click_button(add_loader.passport_toggl)
    add_loader.dropdown_click_input_click(add_loader.loader_country_select, "Азербайджан / Azerbaijan / AZE")
    add_loader.input_in_field(add_loader.loader_city_input, "Баку")
    surname = f"Ф-{add_loader.get_timestamp()}"
    add_loader.input_in_field(add_loader.surname_input, surname)
    add_loader.input_in_field(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.passport_id_input, add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.input_in_field(add_loader.passport_by_input, "Верховный грузила")
    add_loader.input_in_field(add_loader.passport_code_input,
                              add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Упаковщик", 2, 1)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Сборщик", 3, 2)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Штабелерщик", 4, 3)
    add_loader.click_button(add_loader.date_button, index=3)
    add_loader.input_in_field(add_loader.calendar_input, value="10102045")
    add_loader.input_in_field(add_loader.app_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.contact_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.reg_address_input, "Мой адрес – какой то Другой")
    add_loader.backspace_all_and_input(add_loader.fact_address_input, "Мой адрес – какой то Другой")
    add_loader.click_button(add_loader.create_loader_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="lst")
    
    loader_list.input_in_field(loader_list.surname_filter, value=surname, wait="lst")
    loader_list.click_button(loader_list.first_loader_link, wait="form")
    
    add_loader.click_button(add_loader.loader_edit_button, wait="form")
    add_loader.click_button(add_loader.passport_toggl)
    add_loader.backspace_all_and_input(add_loader.surname_input, f"Ф-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.passport_id_input,
                                       add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.backspace_all_and_input(add_loader.passport_by_input, "Главный грузила")
    add_loader.backspace_all_and_input(add_loader.passport_code_input,
                                       add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=3, click_to=add_loader.close_circle_button, click_index=6)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=2, click_to=add_loader.close_circle_button, click_index=5)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=1, click_to=add_loader.close_circle_button, click_index=4)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Грузчик")
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Такелажник", 2, 2)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Стропальщик", 3, 3)
    add_loader.click_button(add_loader.date_button, index=3)
    add_loader.input_in_field(add_loader.calendar_input, value="10102045")
    add_loader.backspace_all_and_input(add_loader.app_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.contact_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.reg_address_input, "Мой адрес – Не дом и не улица")
    add_loader.input_in_field(add_loader.fact_address_input, "Мой адрес – Советский Союз.")
    add_loader.click_button(add_loader.confirm_edit_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="form")
    
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание и редвктирование специалиста')
@allure.description('ЛКП. Тест создания  и редвктирование специалиста ПВ: '
                    '1) создаем: ФИО - ФИО-timestamp, паспорт - РФ, тип - Грузчик/Сборщик/Карщик, '
                    'годен до - 10.10.2045, № паспорт/код/права/тлф.апп/тлф. - Рандом.'
                    '2) редактируем: ФИО - ФИО-timestamp, паспорт - Азербайджан/Баку, тип - Упаковщик/Стропальщик, '
                    'годен до - 10.10.2045, № паспорт/код/права/тлф.апп/тлф. - Рандом.')
def test_loader2_edit_lkp(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkp')
    
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    
    loader_list = LoaderList(base.driver)
    loader_list.click_button(loader_list.add_loader_button, wait="form")
    
    add_loader = LoaderAdd(base.driver)
    surname = f"Ф-{add_loader.get_timestamp()}"
    add_loader.input_in_field(add_loader.surname_input, surname)
    add_loader.input_in_field(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.input_in_field(add_loader.passport_id_input, add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.input_in_field(add_loader.passport_by_input, "Верховный грузила")
    add_loader.input_in_field(add_loader.passport_code_input,
                              add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Грузчик", 1, 1)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Сборщик", 2, 2)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Карщик", 3, 3)
    add_loader.click_button(add_loader.date_button, index=3)
    add_loader.input_in_field(add_loader.calendar_input, value="10102045")
    add_loader.input_in_field(add_loader.app_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.contact_phone_input,
                              add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.input_in_field(add_loader.reg_address_input, "Мой адрес – Не дом и не улица")
    add_loader.input_in_field(add_loader.fact_address_input, "Мой адрес – Советский Союз.")
    add_loader.click_button(add_loader.create_loader_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="lst")
    
    loader_list.input_in_field(loader_list.surname_filter, value=surname, wait="lst")
    loader_list.click_button(loader_list.first_loader_link, wait="form")
    
    add_loader.click_button(add_loader.loader_edit_button, wait="form")
    add_loader.click_button(add_loader.passport_toggl)
    add_loader.dropdown_click_input_click(add_loader.loader_country_select, "Азербайджан / Azerbaijan / AZE")
    add_loader.input_in_field(add_loader.loader_city_input, "Баку")
    add_loader.backspace_all_and_input(add_loader.surname_input, f"Ф-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.name_input, f"И-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.patronymic_input, f"О-{add_loader.get_timestamp()}")
    add_loader.backspace_all_and_input(add_loader.passport_id_input,
                                       add_loader.random_value_float_str(1000000000, 9999999999))
    add_loader.backspace_all_and_input(add_loader.passport_by_input, "Главный грузила")
    add_loader.backspace_all_and_input(add_loader.passport_code_input,
                                       add_loader.random_value_float_str(100000, 999999), click_first=True)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=4, click_to=add_loader.close_circle_button, click_index=6)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=3, click_to=add_loader.close_circle_button, click_index=5)
    add_loader.move_and_click(move_to=add_loader.loader_type_select,
                              move_index=2, click_to=add_loader.close_circle_button, click_index=4)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Упаковщик", 2, 1)
    add_loader.dropdown_click_input_click(add_loader.loader_type_select, "Стропальщик", 3, 2)
    add_loader.click_button(add_loader.date_button, index=3)
    add_loader.input_in_field(add_loader.calendar_input, value="10102045")
    add_loader.backspace_all_and_input(add_loader.app_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.contact_phone_input,
                                       add_loader.random_value_float_str(8650000000, 8659999999), click_first=True)
    add_loader.backspace_all_and_input(add_loader.reg_address_input, "Мой адрес – какой то Другой")
    add_loader.backspace_all_and_input(add_loader.fact_address_input, "Мой адрес – какой то Другой")
    add_loader.click_button(add_loader.confirm_edit_button, do_assert=True)
    add_loader.click_button(add_loader.confirm_add_button, wait="form")
    
    sidebar.test_finish()
    