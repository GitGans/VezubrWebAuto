import allure
import pytest
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList


@allure.story("Critical path test")
@allure.feature('Создание и редактирование водителей')
@allure.description('ЛКП. Тест редактирования водителя: ФИО - ФИО-timestamp, паспорт/права - Другой/Другой, '
                    'страна - Албания, город - Тирана, № паспорт/код/права/тлф.апп/тлф. - Рандом, книжка - Да')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_own_driver1_edit_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button, wait="form")
    
    add_driver = DriverAdd(base.driver)
    # Добавление нового водителя и получение его фамилии
    surname = add_driver.add_base_driver()
    
    # Фильтрация по фамилии водителя и переход к его профилю
    driver_list.input_in_field(driver_list.surname_filter, value=surname, wait="lst")
    driver_list.click_button(driver_list.first_driver_link, wait="form")
    
    # Клик по кнопке редактирования водителя
    add_driver.click_button(add_driver.driver_edit_button, wait="form")
    # Включить тогл паспорт
    add_driver.click_button(add_driver.passport_toggl)
    # Выбор страны - Албания
    add_driver.dropdown_click_input_click(add_driver.driver_country_select, "Албания / Albania / ALB")
    # Ввод города - Тирана
    add_driver.input_in_field(add_driver.driver_city_input, "Тирана")
    # Ввод новой фамилии
    add_driver.backspace_all_and_input(add_driver.surname_input, f"Ф-{base.get_timestamp()}")
    # Ввод нового имени
    add_driver.backspace_all_and_input(add_driver.name_input, f"И-{base.get_timestamp()}")
    # Ввод нового отчества
    add_driver.backspace_all_and_input(add_driver.patronymic_input, f"О-{base.get_timestamp()}")
    # Ввод нового номера паспорта
    add_driver.backspace_all_and_input(add_driver.passport_id_input,
                                       base.random_value_float_str(1000000000, 9999999999))
    # Ввод органа, выдавшего паспорт
    add_driver.backspace_all_and_input(add_driver.passport_by_input, "Верховный водилокомандующий")
    # Ввод кода подразделения паспорта
    add_driver.backspace_all_and_input(add_driver.passport_code_input,
                                       base.random_value_float_str(100000, 999999), click_first=True)
    # Включить тогл права
    add_driver.click_button(add_driver.license_toggl)
    # Ввод органа, выдавшего права
    add_driver.input_in_field(add_driver.license_issued_by_input, "Нерусский кто-то")
    # Ввод места выдачи прав
    add_driver.input_in_field(add_driver.license_issued_please_input, "Тирана")
    # Ввод даты выдачи прав
    add_driver.input_in_field(add_driver.license_issued_date_input, "10102010")
    # Ввод номера прав
    add_driver.backspace_all_and_input(add_driver.license_id_input,
                                       base.random_value_float_str(1000000000, 9999999999), click_first=True)
    # Ввод контактного телефона
    add_driver.backspace_all_and_input(add_driver.contact_phone_input,
                                       base.random_value_float_str(9650000000, 9659999999), click_first=True)
    # Ввод регистрационного адреса
    add_driver.backspace_all_and_input(add_driver.reg_address_input, "Мой адрес – Тирана")
    # Ввод фактического адреса
    add_driver.backspace_all_and_input(add_driver.fact_address_input, "Мой адрес – Албания.")
    # Включить тогл наличия санитарной книжки
    add_driver.click_button(add_driver.sanitary_book_toggl)
    # Закрыть дату окончания санитарной книжки
    add_driver.click_button(add_driver.sanitary_book_date_input_close)
    # Ввод даты начала санитарной книжки
    add_driver.input_in_field(add_driver.sanitary_book_date_input_open, '10102045')
    # Клик по кнопке сохранения изменений
    add_driver.click_button(add_driver.save_button, do_assert=True)
    # Подтверждение успешного сохранения изменений
    add_driver.click_button(add_driver.ok_button, wait="form")
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и редактирование водителей')
@allure.description('ЛКП. Тест редактирования водителя: ФИО - ФИО-timestamp, паспорт/права - РФ/Другой, '
                    'права - Тирана/10.10.10, № паспорт/код/права/тлф.апп/тлф. - Рандом, книжка - Да')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_own_driver2_edit_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button, wait="form")
    
    add_driver = DriverAdd(base.driver)
    # Включить тогл паспорт
    add_driver.click_button(add_driver.passport_toggl)
    # Выбор страны - Албания
    add_driver.dropdown_click_input_click(add_driver.driver_country_select, "Албания / Albania / ALB")
    # Ввод города - Тирана
    add_driver.input_in_field(add_driver.driver_city_input, "Тирана")
    # Добавление нового водителя и получение его фамилии
    surname = add_driver.add_base_driver()
    
    # Фильтрация по фамилии водителя и переход к его профилю
    driver_list.input_in_field(driver_list.surname_filter, value=surname, wait="lst")
    driver_list.click_button(driver_list.first_driver_link, wait="form")
    
    # Клик по кнопке редактирования водителя
    add_driver.click_button(add_driver.driver_edit_button, wait="form")
    # Включить тогл паспорт
    add_driver.click_button(add_driver.passport_toggl)
    # Ввод новой фамилии
    add_driver.backspace_all_and_input(add_driver.surname_input, f"Ф-{base.get_timestamp()}")
    # Ввод нового имени
    add_driver.backspace_all_and_input(add_driver.name_input, f"И-{base.get_timestamp()}")
    # Ввод нового отчества
    add_driver.backspace_all_and_input(add_driver.patronymic_input, f"О-{base.get_timestamp()}")
    # Ввод нового номера паспорта
    add_driver.backspace_all_and_input(add_driver.passport_id_input,
                                       base.random_value_float_str(1000000000, 9999999999))
    # Ввод органа, выдавшего паспорт
    add_driver.backspace_all_and_input(add_driver.passport_by_input, "Верховный водилокомандующий")
    # Ввод кода подразделения паспорта
    add_driver.backspace_all_and_input(add_driver.passport_code_input,
                                       base.random_value_float_str(100000, 999999), click_first=True)
    # Включить тогл права
    add_driver.click_button(add_driver.license_toggl)
    # Ввод органа, выдавшего права
    add_driver.input_in_field(add_driver.license_issued_by_input, "Нерусский кто-то")
    # Ввод места выдачи прав
    add_driver.input_in_field(add_driver.license_issued_please_input, "Тирана")
    # Ввод даты выдачи прав
    add_driver.input_in_field(add_driver.license_issued_date_input, "10102010")
    # Ввод номера прав
    add_driver.backspace_all_and_input(add_driver.license_id_input,
                                       base.random_value_float_str(1000000000, 9999999999), click_first=True)
    # Ввод контактного телефона
    add_driver.backspace_all_and_input(add_driver.contact_phone_input,
                                       base.random_value_float_str(9650000000, 9659999999), click_first=True)
    # Ввод регистрационного адреса
    add_driver.backspace_all_and_input(add_driver.reg_address_input, "Мой адрес – Тирана")
    # Ввод фактического адреса
    add_driver.backspace_all_and_input(add_driver.fact_address_input, "Мой адрес – Албания.")
    # Включить тогл наличия санитарной книжки
    add_driver.click_button(add_driver.sanitary_book_toggl)
    # Закрыть дату окончания санитарной книжки
    add_driver.click_button(add_driver.sanitary_book_date_input_close)
    # Ввод даты начала санитарной книжки
    add_driver.input_in_field(add_driver.sanitary_book_date_input_open, '10102045')
    # Клик по кнопке сохранения изменений
    add_driver.click_button(add_driver.save_button, do_assert=True)
    # Подтверждение успешного сохранения изменений
    add_driver.click_button(add_driver.ok_button, wait="form")
    # Конец теста
    