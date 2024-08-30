import time
import allure
from pages.request_ltl_add_page import LTLAdd
from tests.base_test import base_test_with_login
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.story("Critical path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКЭ. Тест маршрутизации ГМ ГВ: создаем - ГМ ГВ, маршрутизируем - ТС 20т/90м3/ 33пал')
def test_cargo_place_routing_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(2)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор владельца грузоместа "Auto LKZ"
    add_cp.dropdown_click_input_click(add_cp.cargo_place_owner_select, "Auto LKZ")
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
    cp_list.dropdown_click_input_click(cp_list.vehicle_type_select, dd_index=2, option_text="20т / 90м3 / 33пал.")
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

    # Завершение теста
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКЗ. Тест маршрутизации ГМ: создаем - ГМ, маршрутизируем - ТС 20т/90м3/ 33пал')
def test_cargo_place_routing_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
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
    cp_list.dropdown_click_input_click(cp_list.vehicle_type_select, dd_index=2, option_text="20т / 90м3 / 33пал.")
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
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Массовое редактирование грузомест')
@allure.description('ЛКЭ. Тест массового редактирования ГМ ГВ: создаем - родительское ГМ ГВ, выбираем - 2-е и 3-е ГМ в '
                    'списке, статус - Принято, адреса к статусу/отправления/доставки - Первый в списке, родительске ГМ '
                    '- Созданное ГМ с баркодом - cp_stamp')
def test_cargo_place_multi_edit_lke(domain):
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
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lke()
    
    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор второго чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=4)
    # Выбор третьего чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение статуса грузомест
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Статус")
    cp_list.dropdown_click_input_click(cp_list.new_value_select, "Принято")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение адреса к статусу
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Адрес к статусу")
    cp_list.dropdown_click_input_click(cp_list.new_value_select, "15680 / г Екатеринбург, пр-кт Ленина, д 125")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение адреса отправления
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Адрес отправления")
    cp_list.dropdown_click_input_click(cp_list.new_value_select, "15680 / г Екатеринбург, пр-кт Ленина, д 125")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение адреса доставки
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Адрес доставки")
    cp_list.dropdown_click_input_click(cp_list.new_value_select,
                                       "15982 / Свердловская обл, г Березовский, ул Театральная, д 13")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение баркода родительского ГМ
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Баркод родительского ГМ")
    cp_list.input_in_field(cp_list.parent_barcode_input, cp_stamp)
    cp_list.click_button(cp_list.ok_button, wait="lst", do_assert=True)
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Массовое редактирование грузомест')
@allure.description('ЛКЗ. Тест массового редактирования ГМ: создаем - родительское ГМ, выбираем - 2-е и 3-е ГМ в '
                    'списке, статус - Принято, адреса к статусу/отправления/доставки - Первый в списке, родительске ГМ '
                    '- Созданное ГМ с баркодом - cp_stamp')
def test_cargo_place_multi_edit_lkz(domain):
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
    # Добавление полного базового грузоместа
    cp_stamp = add_cp.add_full_cargo_place_lkz()
    
    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор второго чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=4)
    # Выбор третьего чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение статуса грузомест
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Статус")
    cp_list.dropdown_click_input_click(cp_list.new_value_select, "Принято")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение адреса к статусу
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Адрес к статусу")
    cp_list.dropdown_click_input_click(cp_list.new_value_select, "15680 / г Екатеринбург, пр-кт Ленина, д 125")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение адреса отправления
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Адрес отправления")
    cp_list.dropdown_click_input_click(cp_list.new_value_select, "15680 / г Екатеринбург, пр-кт Ленина, д 125")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение адреса доставки
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Адрес доставки")
    cp_list.dropdown_click_input_click(cp_list.new_value_select,
                                       "15982 / Свердловская обл, г Березовский, ул Театральная, д 13")
    cp_list.click_button(cp_list.ok_button, wait="lst")
    # Клик по кнопке редактировать
    cp_list.click_button(cp_list.multi_edit_button)
    # Изменение баркода родительского ГМ
    cp_list.dropdown_click_input_click(cp_list.field_change_select, "Баркод родительского ГМ")
    cp_list.input_in_field(cp_list.parent_barcode_input, cp_stamp)
    cp_list.click_button(cp_list.ok_button, wait="lst", do_assert=True)
    
    # Завершение теста
    sidebar.test_finish()
    
    
@allure.story("Smoke test")
@allure.feature('Передача грузомест экспедитору')
@allure.description('ЛКЭ. Тест передачи ГМ Экспедитору: '
                    'создаем - ГМ ГВ, передаем - Экс, создаем - LTL заявку, публикация - не публикуем')
def test_cargo_place_transfer_lke(domain):
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
    
    ltl = LTLAdd(base.driver)
    # Заполнение базовой информации для LTL заявки
    ltl.add_base_ltl()
    time.sleep(1)
    # Публикация заявки позже
    ltl.click_button(ltl.publish_later_button, do_assert=True)

    # Завершение теста
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Передача грузомест экспедитору')
@allure.description('ЛКЗ. Тест передачи ГМ Экспедитору: '
                    'создаем - ГМ ГВ, передаем - Экс, создаем - LTL заявку, публикация - не публикуем')
def test_cargo_place_transfer_lkz(domain):
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
    
    ltl = LTLAdd(base.driver)
    # Заполнение базовой информации для LTL заявки
    ltl.add_base_ltl()
    time.sleep(1)
    # Публикация заявки позже
    ltl.click_button(ltl.publish_later_button, do_assert=True)
    
    # Завершение теста
    sidebar.test_finish()
    