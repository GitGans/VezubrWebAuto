import allure
from tests.base_test import base_test_with_login
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList


@allure.epic("Стабильные тесты")
@allure.story("Critical path test")
@allure.feature('Редактирование водителей')
@allure.description('ЛКЭ. Тест редактирования собственного водителя Экс: ФИО - ФИО-timestamp, паспорт/права - '
                    'Другой/РФ, страна - Албания, город - Тирана, № паспорт/код/права/тлф.апп/тлф. - Рандом.'
                    'книжка - Да')
def test_own_driver_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                                do_assert=True, wait="lst")

    driver_list = DriverList(base.driver)
    driver_list.click_button(driver_list.add_driver_button, wait="form")

    add_driver = DriverAdd(base.driver)
    add_driver.add_base_driver()

    driver_list.click_button(driver_list.first_driver_link, wait="form")

    add_driver.click_button(add_driver.driver_edit_button, wait="form")
    add_driver.click_button(add_driver.passport_toggl)
    add_driver.dropdown_click_input_click(add_driver.driver_country_select, "Албания / Albania / ALB")
    add_driver.input_in_field(add_driver.driver_city_input, "Тирана")
    add_driver.backspace_len_and_input(add_driver.surname_input, f"Ф-{base.get_timestamp()}")
    add_driver.backspace_len_and_input(add_driver.name_input, f"И-{base.get_timestamp()}")
    add_driver.backspace_len_and_input(add_driver.patronymic_input, f"О-{base.get_timestamp()}")
    add_driver.backspace_len_and_input(add_driver.passport_id_input, base.random_value_int_str(1000000000, 9999999999))
    add_driver.backspace_len_and_input(add_driver.passport_by_input, "Верховный водилокомандующий")
    add_driver.backspace_len_and_input(add_driver.passport_code_input, base.random_value_int_str(100000, 999999))
    add_driver.backspace_len_and_input(add_driver.license_id_input, base.random_value_int_str(1000000000, 9999999999))
    add_driver.backspace_len_and_input(add_driver.contact_phone_input,
                                       base.random_value_int_str(9650000000, 9659999999))
    add_driver.backspace_len_and_input(add_driver.reg_address_input, "Мой адрес – Тирана")
    add_driver.backspace_len_and_input(add_driver.fact_address_input, "Мой адрес – Албания.")
    add_driver.click_button(add_driver.sanitary_book_toggl)
    add_driver.click_button(add_driver.sanitary_book_date_input_close)
    add_driver.input_in_field(add_driver.sanitary_book_date_input_open, '10102045')
    add_driver.click_button(add_driver.save_button, do_assert=True, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Critical path test")
@allure.feature('Редактирование водителей')
@allure.description('ЛКЭ. Тест редактирования водителя внутр КА: ка - Первый в списке, ФИО - ВФИО-timestamp, '
                    'паспорт/права - РФ/Другой, № паспорт/код/права/тлф. - Рандомб, книжка - Да')
def test_inner_driver_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                                do_assert=True, wait="lst")

    driver_list = DriverList(base.driver)
    driver_list.click_button(driver_list.add_driver_button, wait="form")

    add_driver = DriverAdd(base.driver)
    add_driver.add_base_inner_driver()

    driver_list.click_button(driver_list.first_driver_link, wait="form")

    add_driver.click_button(add_driver.driver_edit_button, wait="form")
    add_driver.backspace_len_and_input(add_driver.surname_input, f"ВФ-{base.get_timestamp()}")
    add_driver.backspace_len_and_input(add_driver.name_input, f"ВИ-{base.get_timestamp()}")
    add_driver.backspace_len_and_input(add_driver.patronymic_input, f"ВО-{base.get_timestamp()}")
    add_driver.backspace_len_and_input(add_driver.passport_id_input, base.random_value_int_str(1000000000, 9999999999))
    add_driver.backspace_len_and_input(add_driver.passport_by_input, "Верховный водилокомандующий")
    add_driver.backspace_len_and_input(add_driver.passport_code_input, base.random_value_int_str(100000, 999999))
    add_driver.click_button(add_driver.license_toggl)
    add_driver.input_in_field(add_driver.license_issued_by_input, "Нерусский кто-то")
    add_driver.input_in_field(add_driver.license_issued_please_input, "Другой")
    add_driver.input_in_field(add_driver.license_issued_date_input, "10102010")
    add_driver.backspace_len_and_input(add_driver.license_id_input, base.random_value_int_str(1000000000, 9999999999))
    add_driver.backspace_len_and_input(add_driver.contact_phone_input,
                                       base.random_value_int_str(9650000000, 9659999999))
    add_driver.backspace_len_and_input(add_driver.reg_address_input, "Мой адрес – Другой.")
    add_driver.backspace_len_and_input(add_driver.fact_address_input, "Мой адрес – Другой.")
    add_driver.click_button(add_driver.sanitary_book_toggl)
    add_driver.click_button(add_driver.sanitary_book_date_input_close)
    add_driver.input_in_field(add_driver.sanitary_book_date_input_open, '10102045')
    add_driver.click_button(add_driver.save_button, do_assert=True, wait="lst")

    sidebar.finish_test()