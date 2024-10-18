import time
import allure
import pytest
from pages.agreement_add_page import AgreementAdd
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor


@allure.story("Critical path test")
@allure.feature('Создание договоров')
@allure.description('ЛКП. Тест создания договора с ГВ: '
                    'номер - №-timestamp, срок - с Сегодня по 45 год, автоформирование реестров - Отключено.')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_agreement_client_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку клиентов
    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lkz_inn"
    client_list.click_button(client_list.client_lkz_inn, wait="form")

    contractor = Contractor(base.driver)
    # Клик по кнопке добавления договора
    contractor.click_button(contractor.add_agreements_button)

    add_agr = AgreementAdd(base.driver)
    # Ввод номера договора
    add_agr.input_in_field(add_agr.agr_number_input, f"№-{base.get_timestamp()}")
    # Установка даты начала договора на сегодня
    add_agr.click_button(add_agr.agr_add_date_button)
    add_agr.click_button(add_agr.today_button)
    # Установка даты окончания договора на 01.01.2045
    add_agr.click_button(add_agr.agr_end_date_button)
    time.sleep(0.5)
    add_agr.input_in_field(add_agr.agr_date_input, "01012045")
    # Отключение автоматического формирования реестров
    add_agr.dropdown_without_input(add_agr.registers_auto_select, "Автоматическое формирование Реестров отключено")
    # Клик по кнопке добавления договора
    add_agr.click_button(add_agr.add_agr_button, do_assert=True)
    # Клик по кнопке подтверждения добавления договора
    add_agr.click_button(add_agr.confirm_add_button)
    # Конец теста
    