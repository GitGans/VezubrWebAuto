import time

import allure
from tests.base_test import base_test_with_login
from pages.address_add_page import AddressAdd
from pages.address_list_page import AddressesList


@allure.story("Smoke test")
@allure.feature('Создание адресов')
@allure.description('ЛКЭ. Тест создания адреса: статус - Активный, ввод адреса в поле Фактический адрес.')
def test_address_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку адресов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    
    address_list = AddressesList(base.driver)
    # Клик по кнопке добавления адреса
    address_list.click_button(address_list.add_address_button)
    
    add_address = AddressAdd(base.driver)
    # Установка статуса адреса в "Активный"
    add_address.click_button(add_address.address_status_toggl)
    # Ввод фактического адреса и выбор из выпадающего списка
    add_address.dropdown_click_input_wait_enter(
        add_address.address_input,
        f"г Екатеринбург, пр-кт Ленина, д {base.random_value_float_str(1, 150)}",
        wait_presence=True
    )
    # Ожидание подгрузки данных от DaData
    time.sleep(1)
    # Клик по кнопке создания адреса
    add_address.click_button(add_address.create_address_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_address.click_button(add_address.confirm_add_button, wait="lst")
    
    # Завершение теста
    sidebar.test_finish()
