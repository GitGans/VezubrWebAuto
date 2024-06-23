import time
import allure
from tests.base_test import base_test_with_login
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.story("Smoke test")
@allure.feature('Создание грузомест')
@allure.description('ЛКЭ. Тест создания ГМ ГВ: тип - Короб, кол-во/вес/объем/цена/температура - Рандом, статус - Новое,'
                    ' название/накладная/штрихкод/пломба/внешний id - ГМ-timestamp, адреса - Первые из списка.')
def test_cargo_place_from_lkz_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор владельца грузоместа "Auto LKZ"
    add_cp.dropdown_click_input_click(add_cp.cargo_place_owner_select, "Auto LKZ")
    # Выбор типа грузоместа "Короб"
    add_cp.dropdown_click_input_click(add_cp.lke_cp_type_select, "Короб")
    # Ввод рандомизированных данных для количества, веса, объема и стоимости груза
    add_cp.input_in_field(add_cp.cp_quantity_input, add_cp.random_value_float_str(1, 10))
    add_cp.input_in_field(add_cp.cp_weight_input, add_cp.random_value_float_str(10, 20000))
    add_cp.input_in_field(add_cp.cp_value_input, add_cp.random_value_float_str(0.1, 35.0))
    add_cp.input_in_field(add_cp.cp_cost_input, add_cp.random_value_float_str(100, 1000000))
    # Выбор статуса грузоместа "Новое"
    add_cp.dropdown_click_input_click(add_cp.lke_cp_status_select, "Новое")
    # Генерация уникального идентификатора для грузоместа
    cp_stamp = f"ГМ-{add_cp.get_timestamp()}"
    # Ввод уникальных данных для грузоместа
    add_cp.input_in_field(add_cp.lke_cp_title_input, cp_stamp)  # Название
    add_cp.input_in_field(add_cp.lke_invoice_number_input, cp_stamp)  # Номер накладной
    add_cp.input_in_field(add_cp.lke_bar_code_input, cp_stamp)  # Штрихкод
    add_cp.input_in_field(add_cp.lke_seal_number_input, cp_stamp)  # Номер пломбы
    add_cp.input_in_field(add_cp.temp_from_input, add_cp.random_value_float_str(-5, 0))  # Температура от
    add_cp.input_in_field(add_cp.temp_until_input, add_cp.random_value_float_str(0, 5))  # Температура до
    add_cp.input_in_field(add_cp.lke_external_id_input, cp_stamp)  # Внешний ID
    add_cp.input_in_field(add_cp.lke_comment_input, cp_stamp)  # Комментарий
    # Ввод адресов отправления и доставки
    add_cp.dropdown_click_input_wait_enter(add_cp.departure_address_select, "Auto LKZ")
    add_cp.dropdown_click_input_wait_enter(add_cp.delivery_address_select, "Auto LKZ")
    # Клик по кнопке создания грузоместа
    add_cp.click_button(add_cp.create_cargo_place_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_cp.click_button(add_cp.confirm_add_button, wait="lst")
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание и удаление грузомест')
@allure.description('ЛКЭ. Тест создания ГМ Экс с влож ГМ ГВ:  тип - Короб, кол-во/вес/объем/цена/температура - Рандом, '
                    'статус - Новое, название/накладная/штрихкод/пломба/внешний id - ГМ-timestamp, '
                    'адреса - Первые из списка, гм - Удаляем')
def test_cargo_place_own_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор владельца грузоместа "Собственное Задание Экспедитора"
    add_cp.dropdown_click_input_click(add_cp.cargo_place_owner_select, "Собственное Задание Экспедитора")
    # Выбор вложенного грузоместа
    add_cp.click_button(add_cp.child_cp_select, wait="lst")
    # Очистка даты и выбор грузоместа
    cp_list.move_and_click(move_to=cp_list.date_hover, click_to=cp_list.date_clear_button, wait="lst")
    cp_list.click_button(cp_list.cp_list_checkbox, index=2)
    cp_list.click_button(cp_list.confirm_button)
    # Выбор типа грузоместа "Короб"
    add_cp.dropdown_click_input_click(add_cp.lke_cp_type_select, "Короб")
    # Ввод рандомизированных данных для количества, веса, объема и стоимости груза
    add_cp.backspace_len_and_input(add_cp.cp_quantity_input, base.random_value_float_str(1, 10))
    add_cp.backspace_len_and_input(add_cp.cp_weight_input, base.random_value_float_str(10, 20000))
    add_cp.backspace_len_and_input(add_cp.cp_value_input, base.random_value_float_str(0.1, 35.0))
    add_cp.backspace_len_and_input(add_cp.cp_cost_input, base.random_value_float_str(100, 1000000))
    # Выбор статуса грузоместа "Новое"
    add_cp.dropdown_click_input_click(add_cp.lke_cp_status_select, "Новое")
    # Генерация уникального идентификатора для грузоместа
    cp_stamp = f"ГМ-{add_cp.get_timestamp()}"
    # Ввод уникальных данных для грузоместа
    add_cp.input_in_field(add_cp.lke_cp_title_input, cp_stamp)  # Название
    add_cp.input_in_field(add_cp.lke_invoice_number_input, cp_stamp)  # Номер накладной
    add_cp.input_in_field(add_cp.lke_bar_code_input, cp_stamp)  # Штрихкод
    add_cp.input_in_field(add_cp.lke_seal_number_input, cp_stamp)  # Номер пломбы
    add_cp.input_in_field(add_cp.temp_from_input, add_cp.random_value_float_str(-5, 0))  # Температура от
    add_cp.input_in_field(add_cp.temp_until_input, add_cp.random_value_float_str(0, 5))  # Температура до
    add_cp.input_in_field(add_cp.lke_external_id_input, cp_stamp)  # Внешний ID
    add_cp.input_in_field(add_cp.lke_comment_input, cp_stamp)  # Комментарий
    # Ввод адресов отправления и доставки
    add_cp.dropdown_click_input_wait_enter(add_cp.departure_address_select, "Auto LKE")
    add_cp.dropdown_click_input_wait_enter(add_cp.delivery_address_select, "Auto LKE")
    # Клик по кнопке создания грузоместа
    add_cp.click_button(add_cp.create_cargo_place_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_cp.click_button(add_cp.confirm_add_button, wait="lst")
    
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по ссылке первого грузоместа в списке
    cp_list.click_button(cp_list.first_cp_link, wait="form")
    
    # Удаление созданного грузоместа
    add_cp.click_button(add_cp.delete_button, do_assert=True)
    # Подтверждение удаления грузоместа
    add_cp.click_button(add_cp.yes_button)
    # Подтверждение успешного удаления
    add_cp.click_button(add_cp.ok_button, wait="lst")

    # Завершение теста
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание и удаление грузомест')
@allure.description('ЛКЗ. Тест создания ГМ: тип - Короб, кол-во/вес/объем/цена/температура - Рандом, статус - Новое, '
                    'название/накладная/штрихкод/пломба/внешний id - ГМ-timestamp, адреса - Первые из списка, '
                    'гм - Удаляем')
def test_cargo_place_add_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор типа грузоместа "Короб"
    add_cp.dropdown_click_input_click(add_cp.lkz_cp_type_select, "Короб")
    # Ввод рандомизированных данных для количества, веса, объема и стоимости груза
    add_cp.input_in_field(add_cp.cp_quantity_input, add_cp.random_value_float_str(1, 10))
    add_cp.input_in_field(add_cp.cp_weight_input, add_cp.random_value_float_str(10, 20000))
    add_cp.input_in_field(add_cp.cp_value_input, add_cp.random_value_float_str(0.1, 35.0))
    add_cp.input_in_field(add_cp.cp_cost_input, add_cp.random_value_float_str(100, 1000000))
    # Выбор статуса грузоместа "Новое"
    add_cp.dropdown_click_input_click(add_cp.lkz_cp_status_select, "Новое")
    # Генерация уникального идентификатора для грузоместа
    cp_stamp = f"ГМ-{add_cp.get_timestamp()}"
    # Ввод уникальных данных для грузоместа
    add_cp.input_in_field(add_cp.lkz_cp_title_input, cp_stamp)  # Название
    add_cp.input_in_field(add_cp.lkz_invoice_number_input, cp_stamp)  # Номер накладной
    add_cp.input_in_field(add_cp.lkz_bar_code_input, cp_stamp)  # Штрихкод
    add_cp.input_in_field(add_cp.lkz_seal_number_input, cp_stamp)  # Номер пломбы
    add_cp.input_in_field(add_cp.temp_from_input, add_cp.random_value_float_str(-5, 0))  # Температура от
    add_cp.input_in_field(add_cp.temp_until_input, add_cp.random_value_float_str(0, 5))  # Температура до
    add_cp.input_in_field(add_cp.lkz_external_id_input, cp_stamp)  # Внешний ID
    add_cp.input_in_field(add_cp.lkz_comment_input, cp_stamp)  # Комментарий
    # Ввод адресов отправления и доставки
    add_cp.dropdown_click_input_wait_enter(add_cp.departure_address_select, "Екатеринбург")
    add_cp.dropdown_click_input_wait_enter(add_cp.delivery_address_select, "Екатеринбург")
    # Клик по кнопке создания грузоместа
    add_cp.click_button(add_cp.create_cargo_place_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_cp.click_button(add_cp.confirm_add_button, wait="lst")
    
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по ссылке первого грузоместа в списке
    cp_list.click_button(cp_list.first_cp_link, wait="form")
    
    # Удаление созданного грузоместа
    add_cp.click_button(add_cp.delete_button, do_assert=True)
    # Подтверждение удаления грузоместа
    add_cp.click_button(add_cp.yes_button)
    # Подтверждение успешного удаления
    add_cp.click_button(add_cp.ok_button, wait="lst")
    
    # Завершение теста
    sidebar.test_finish()
