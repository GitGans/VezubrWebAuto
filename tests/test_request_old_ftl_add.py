import time
import allure
import pytest
from pages.request_old_ftl_add_page import FTLAdd


@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('ЛКЭ. Тест создания FTL заявки от ГВ: тип - Город, подача - Сейчас, ТС - Груз 0.5т, '
                    'кузов - Закрытый, адреса - Конкретные, публикация - Тариф')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_ftl_request_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)

    ftl = FTLAdd(base.driver)
    # Сброс ранее введенных и сохраненных данных
    ftl.click_button(ftl.cancel_button)
    
    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    
    # Выбор владельца заявки
    ftl.dropdown_click_input_click(ftl.request_owner_select, "Auto LKZ")
    # Установка даты подачи заявки на сегодня
    ftl.click_button(ftl.start_date_field)
    ftl.click_button(ftl.today_button)
    # Установка времени подачи заявки через 30 минут от текущего времени
    ftl.click_button(ftl.start_time_field)
    new_time = ftl.naw_time_change(30)
    ftl.input_in_field(ftl.start_time_input, new_time)
    time.sleep(1)
    # Выбор категории заявки - Груз
    ftl.click_button(ftl.request_category_select)
    ftl.click_button(ftl.select_freight)
    # Выбор типа ТС - до 0.5т
    ftl.dropdown_click_input_wait_enter(ftl.vehicle_type_select, "до 0.5т")
    # Выбор типа кузова - Закрытый
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)
    # Выбор первого адреса из списка
    ftl.click_button(ftl.first_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Березовский, ул Театральная, д 13", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием тарифа
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.producer_select)
    ftl.click_button(ftl.producer_check_box, index=2)
    ftl.click_button(ftl.producer_select_text)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)
    ftl.click_button(ftl.confirm_add_button, wait="lst")
    # Конец теста
    
    
@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('ЛКЗ. Тест создания FTL заявки: тип - Город, подача - Сейчас, ТС - Груз 0.5т, '
                    'кузов - Закрытый, адреса - Конкретные, публикация - Тариф')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_ftl_request_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    
    ftl = FTLAdd(base.driver)
    # Сброс ранее введенных и сохраненных данных
    ftl.click_button(ftl.cancel_button)
    
    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    
    # Установка даты подачи заявки на сегодня
    ftl.click_button(ftl.start_date_field)
    ftl.click_button(ftl.today_button)
    # Установка времени подачи заявки через 30 минут от текущего времени
    ftl.click_button(ftl.start_time_field)
    new_time = ftl.naw_time_change(30)
    ftl.input_in_field(ftl.start_time_input, new_time)
    time.sleep(1)
    # Выбор категории заявки - Груз
    ftl.click_button(ftl.request_category_select)
    ftl.click_button(ftl.select_freight)
    # Выбор типа ТС - до 0.5т
    ftl.click_button(ftl.vehicle_type_select)
    ftl.dropdown_click_input_wait_enter(ftl.vehicle_type_select, "до 0.5т")
    # Выбор типа кузова - Закрытый
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)
    # Выбор первого адреса из списка
    ftl.click_button(ftl.first_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Верхняя Пышма, Успенский пр-кт, д 103а", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.input_in_field(ftl.address_filter, "Свердловская обл, г Березовский, ул Театральная, д 13", wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием тарифа
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.producer_select)
    ftl.click_button(ftl.select_all_producer)
    ftl.click_button(ftl.producer_select_text)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)
    ftl.click_button(ftl.confirm_add_button, wait="lst")
    # Конец теста
