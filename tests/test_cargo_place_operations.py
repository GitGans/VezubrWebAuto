import time
import allure
import pytest
from pages.request_delivery_add_page import DeliveryAdd
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.story("Critical path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКЭ. Тест маршрутизации ГМ ГВ: создаем - ГМ ГВ, маршрутизируем - ТС 20т/90м3/ 33пал')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_cargo_place_routing_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор владельца грузоместа "Auto LKZ"
    add_cp.dropdown_without_input(add_cp.cargo_place_owner_select, "Auto LKZ")
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_base_cargo_place_lke()

    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор первого чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке маршрутизировать ГМ
    cp_list.click_button(cp_list.multi_route_button)
    # Выбор типа ТС для маршрутизации
    cp_list.dropdown_without_input(cp_list.vehicle_type_select, dd_index=2, option_text="20т / 90м3 / 33пал.")
    # Ввод кол-ва ТС для маршрутизации
    cp_list.input_in_field(cp_list.quantity_vehicle_input, "1")
    # Выбор временного периода для маршрутизации ГМ от сегодня
    cp_list.click_button(cp_list.calendar_picker_button)
    cp_list.click_button(cp_list.today_button)
    # Выбор временного периода для маршрутизации ГМ до сегодня + час
    new_time = cp_list.naw_time_change(300)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    time.sleep(1)
    cp_list.click_button(cp_list.today_button)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    cp_list.backspace_num_and_input(cp_list.calendar_input, num=5, value=new_time)
    cp_list.click_button(cp_list.calendar_ok_button)
    # Клик по кнопке отправить ГМ на маршрутизацию
    cp_list.click_button(cp_list.send_button, do_assert=True)
    # Подтверждение успешного отправления на маршрутизацию
    cp_list.click_button(cp_list.ok_button)
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКЗ. Тест маршрутизации ГМ: создаем - ГМ, маршрутизируем - ТС 20т/90м3/ 33пал')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_cargo_place_routing_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_base_cargo_place_lkz()
    
    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор первого чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке маршрутизировать ГМ
    cp_list.click_button(cp_list.multi_route_button)
    # Выбор типа ТС для маршрутизации
    cp_list.dropdown_without_input(cp_list.vehicle_type_select, dd_index=2, option_text="20т / 90м3 / 33пал.")
    # Ввод кол-ва ТС для маршрутизации
    cp_list.input_in_field(cp_list.quantity_vehicle_input, "1")
    # Выбор временного периода для маршрутизации ГМ от сегодня
    cp_list.click_button(cp_list.calendar_picker_button)
    cp_list.click_button(cp_list.today_button)
    # Выбор временного периода для маршрутизации ГМ до сегодня + час
    new_time = cp_list.naw_time_change(300)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    time.sleep(1)
    cp_list.click_button(cp_list.today_button)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    cp_list.backspace_num_and_input(cp_list.calendar_input, num=5, value=new_time)
    cp_list.click_button(cp_list.calendar_ok_button)
    # Клик по кнопке отправить ГМ на маршрутизацию
    cp_list.click_button(cp_list.send_button, do_assert=True)
    # Подтверждение успешного отправления на маршрутизацию
    cp_list.click_button(cp_list.ok_button)
    # Конец теста
    
    
@allure.story("Smoke test")
@allure.feature('Передача грузомест экспедитору')
@allure.description('ЛКЭ. Тест передачи ГМ Экспедитору: '
                    'создаем - ГМ ГВ, передаем - Экс, создаем - LTL заявку, публикация - не публикуем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_cargo_place_transfer_lke(base_fixture, domain):
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
    add_cp.dropdown_without_input(add_cp.cargo_place_owner_select, "Auto LKZ")
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_base_cargo_place_lke()
    
    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор первого чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке передать экспедитору
    cp_list.click_button(cp_list.multi_transfer_button)
    
    ltl = DeliveryAdd(base.driver)
    # Заполнение базовой информации для LTL заявки
    ltl.add_base_ltl()
    time.sleep(1)
    # # Сохранение введенных параметров
    # ltl.click_button(ltl.save_button)
    # # Публикация заявки позже
    # ltl.click_button(ltl.publish_later_button, do_assert=True)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Передача грузомест экспедитору')
@allure.description('ЛКЗ. Тест передачи ГМ Экспедитору: '
                    'создаем - ГМ ГВ, передаем - Экс, создаем - LTL заявку, публикация - не публикуем')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_cargo_place_transfer_lkz(base_fixture, domain):
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
    cp_stamp = add_cp.add_base_cargo_place_lkz()
    
    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор первого чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке передать экспедитору
    cp_list.click_button(cp_list.multi_transfer_button)
    
    ltl = DeliveryAdd(base.driver)
    # Заполнение базовой информации для LTL заявки
    ltl.add_base_ltl()
    time.sleep(1)
    # Сохранение введенных параметров
    ltl.click_button(ltl.save_button)
    # Публикация заявки позже
    ltl.click_button(ltl.publish_later_button, do_assert=True)
    # Конец теста
    