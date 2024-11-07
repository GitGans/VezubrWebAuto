import time
import allure
import pytest
from pages.agreement_add_page import AgreementAdd
from pages.contractor_page import Contractor
from pages.producers_list_page import ProducersList


@allure.story("Critical path test")
@allure.feature('Создание договоров')
@allure.description('ЛКЗ. Тест создания договора с ПВ: '
                    'номер - №-timestamp, срок - с Сегодня по 45 год, автоформирование реестров - Отключено.')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_agreement_producer_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку перевозчиков
    sidebar.click_button(sidebar.producers_list_button, do_assert=True, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Клик по перевозчику с ИНН "producer_logo_inn"
    producer_list.click_button(producer_list.producer_logo_inn, wait="form")
    
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
    # Клик по кнопке экшен меню
    add_agr.click_button(add_agr.action_button)
    # Выбор пункта Договор прекращен
    add_agr.click_button(add_agr.termination_contract_button)
    time.sleep(1.5)
    # Проверка даты действия договора
    data = add_agr.naw_time_change(0, 'date_dot')
    add_agr.assert_element_text(add_agr.agr_date_finish, data, wait_type='visible')
    # Конец теста
    