import time
import allure
from tests.base_test import base_test_with_login
from pages.request_ftl_add_page import FTLAdd


@allure.story("Smoke test")
@allure.feature('Создание FTL заявок')
@allure.description('ЛКЭ. Тест создания FTL заявки от ГВ: тип - Город, подача - Сейчас, ТС - Груз 0.5т, '
                    'кузов - Закрытый, адреса - Первые в списке, публикация - Тариф')
def test_ftl_request_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    # Переход к созданию новой FTL заявки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True, wait="form")

    ftl = FTLAdd(base.driver)
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
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(2)
    # Выбор второго адреса из списка
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    # Ожидание завершения расчета стоимости
    base.get_element(ftl.calculate_finish)
    # Публикация заявки с использованием тарифа
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)
    ftl.click_button(ftl.confirm_add_button, wait="lst")

    # Завершение теста
    sidebar.test_finish()
