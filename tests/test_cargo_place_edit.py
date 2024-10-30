import time
import allure
import pytest
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.story("Critical path test")
@allure.feature('Создание и редактирование грузомест')
@allure.description('ЛКЭ. Тест создания и редактирования ГМ Экс с влож ГМ ГВ: '
                    '1) создаем ГМ ГВ: тип - Короб, кол-во/вес/объем/цена/температура - Рандом, статус - Новое,'
                    ' название/накладная/штрихкод/пломба/внешнийid/коммент - ГМ-timestamp, адреса - Первые из списка.'
                    '2) создаем ГМ Экс с влож: тип - Короб, кол-во/вес/объем/цена/температура - Рандом, статус - Новое,'
                    ' название/накладная/штрихкод/пломба/внешнийid/коммент - ГМ-timestamp, адреса - Первые из списка. '
                    '3) редактируем: кол-во/вес/объем/цена/температура - Рандом, '
                    'название/накладная/штрихкод/пломба/внешнийid/коммент - ГМ-timestamp')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_cargo_place_edit_own_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Шаг 1: Создание грузоместа ГВ
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор владельца грузоместа "Auto LKZ"
    add_cp.dropdown_without_input(add_cp.cargo_place_owner_select, "Auto LKZ")
    # Добавление полного базового грузоместа
    add_cp.add_full_cargo_place_lke()
    
    time.sleep(1.5)
    # Шаг 2: Создание грузоместа Экс с вложенным грузоместом
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    # Выбор владельца грузоместа "Собственное Задание Экспедитора"
    add_cp.dropdown_without_input(add_cp.cargo_place_owner_select, "Собственное Задание Экспедитора")
    # Выбор вложенного грузоместа
    add_cp.click_button(add_cp.child_cp_select, wait="lst")
    
    # Очистка даты и выбор грузоместа
    cp_list.move_and_click(move_to=cp_list.date_hover, click_to=cp_list.date_clear_button, wait="lst")
    cp_list.click_button(cp_list.cp_list_checkbox, index=2)
    cp_list.click_button(cp_list.confirm_button)
    
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lke()
    
    # Шаг 3: Редактирование грузоместа
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по ссылке первого грузоместа в списке
    cp_list.click_button(cp_list.first_cp_link, wait="form")
    
    # Клик по кнопке редактирования грузоместа
    add_cp.click_button(add_cp.edit_button)
    # Ввод рандомизированных данных для количества, веса, объема и стоимости груза
    add_cp.backspace_and_input(add_cp.quantity_edit, base.random_value_float_str(1, 10))
    add_cp.backspace_and_input(add_cp.weight_edit, base.random_value_float_str(10, 20000))
    add_cp.backspace_and_input(add_cp.value_edit, base.random_value_float_str(0.1, 35.0, precision=1))
    add_cp.backspace_and_input(add_cp.cost_edit, base.random_value_float_str(100, 1000000))
    # Генерация уникального идентификатора для грузоместа
    cp_stamp = f"ГМ-{add_cp.get_timestamp()}"
    # Ввод уникальных данных для грузоместа
    add_cp.backspace_and_input(add_cp.lke_cp_title_edit, cp_stamp)  # Название
    add_cp.backspace_and_input(add_cp.lke_invoice_number_edit, cp_stamp)  # Номер накладной
    add_cp.backspace_and_input(add_cp.lke_bar_code_edit, cp_stamp)  # Штрихкод
    add_cp.backspace_and_input(add_cp.lke_seal_number_edit, cp_stamp)  # Номер пломбы
    add_cp.backspace_and_input(add_cp.temp_from_edit, add_cp.random_value_float_str(-5, 0))  # Температура от
    add_cp.backspace_and_input(add_cp.temp_until_edit, add_cp.random_value_float_str(0, 5))  # Температура до
    add_cp.backspace_and_input(add_cp.lke_external_id_edit, cp_stamp)  # Внешний ID
    add_cp.backspace_and_input(add_cp.lke_comment_edit, cp_stamp)  # Комментарий
    # Клик по кнопке сохранения изменений
    add_cp.click_button(add_cp.save_button, wait="form")
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание и редактирование грузомест')
@allure.description('ЛКЗ. Тест создания и редактирования ГМ ГВ: '
                    '1) создаем ГМ ГВ: тип - Короб, кол-во/вес/объем/цена/температура - Рандом, статус - Новое,'
                    ' название/накладная/штрихкод/пломба/внешнийid/коммент - ГМ-timestamp, адреса - Первые из списка. '
                    '2) редактируем: кол-во/вес/объем/цена/температура - Рандом, '
                    'название/накладная/штрихкод/пломба/внешнийid/коммент - ГМ-timestamp')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_cargo_place_edit_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Шаг 1: Создание грузоместа
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lkz()
    
    # Шаг 2: Редактирование грузоместа
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по ссылке первого грузоместа в списке
    cp_list.click_button(cp_list.first_cp_link, wait="form")
    
    # Клик по кнопке редактирования грузоместа
    add_cp.click_button(add_cp.edit_button)
    # Ввод рандомизированных данных для количества, веса, объема и стоимости груза
    add_cp.backspace_and_input(add_cp.quantity_edit, base.random_value_float_str(1, 10))
    add_cp.backspace_and_input(add_cp.weight_edit, base.random_value_float_str(10, 20000))
    add_cp.backspace_and_input(add_cp.value_edit, base.random_value_float_str(0.1, 35.0, precision=1))
    add_cp.backspace_and_input(add_cp.cost_edit, base.random_value_float_str(100, 1000000))
    # Генерация уникального идентификатора для грузоместа
    cp_stamp = f"ГМ-{add_cp.get_timestamp()}"
    # Ввод уникальных данных для грузоместа
    add_cp.backspace_and_input(add_cp.lkz_cp_title_edit, cp_stamp)  # Название
    add_cp.backspace_and_input(add_cp.lkz_invoice_number_edit, cp_stamp)  # Номер накладной
    add_cp.backspace_and_input(add_cp.lkz_bar_code_edit, cp_stamp)  # Штрихкод
    add_cp.backspace_and_input(add_cp.lkz_seal_number_edit, cp_stamp)  # Номер пломбы
    add_cp.backspace_and_input(add_cp.temp_from_edit, add_cp.random_value_float_str(-5, 0))  # Температура от
    add_cp.backspace_and_input(add_cp.temp_until_edit, add_cp.random_value_float_str(0, 5))  # Температура до
    add_cp.backspace_and_input(add_cp.lkz_external_id_edit, cp_stamp)  # Внешний ID
    add_cp.backspace_and_input(add_cp.lkz_comment_edit, cp_stamp)  # Комментарий
    # Клик по кнопке сохранения изменений
    add_cp.click_button(add_cp.save_button, wait="form")
    # Конец теста
