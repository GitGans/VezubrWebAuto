import time
import allure
import pytest
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.story("Smoke test")
@allure.feature('Создание грузомест')
@allure.description('ЛКЭ. Тест создания ГМ ГВ: тип - Короб, кол-во/вес/объем/цена/температура - Рандом, статус - Новое,'
                    ' название/накладная/штрихкод/пломба/внешний id - ГМ-timestamp, адреса - Первые из списка.')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_cargo_place_from_lkz_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
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
    # Добавление полного базового грузоместа
    add_cp.add_full_cargo_place_lke()
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и удаление грузомест')
@allure.description('ЛКЭ. Тест создания ГМ Экс с влож ГМ ГВ:  тип - Короб, кол-во/вес/объем/цена/температура - Рандом, '
                    'статус - Новое, название/накладная/штрихкод/пломба/внешний id - ГМ-timestamp, '
                    'адреса - Первые из списка, гм - Удаляем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_cargo_place_own_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
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
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lke()
    
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
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и удаление грузомест')
@allure.description('ЛКЗ. Тест создания ГМ: тип - Короб, кол-во/вес/объем/цена/температура - Рандом, статус - Новое, '
                    'название/накладная/штрихкод/пломба/внешний id - ГМ-timestamp, адреса - Первые из списка, '
                    'гм - Удаляем')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_cargo_place_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lkz()
    
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
    # Конец теста
