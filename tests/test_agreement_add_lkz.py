import time
import allure
from tests.base_test import base_test
from pages.agreement_add_page import AgreementAdd
from pages.contractor_page import Contractor
from pages.produsers_list_page import ProdusersList


@allure.feature('Создание договоров')
@allure.description('ЛКЗ. Тест создания договора с ПВ: '
                    'номер - №-timestamp, срок - с Сегодня по 45 год, автоформирование реестров - Отключено.')
def test_agreement_producer_add_lkz(domain):
    base, sidebar = base_test(domain=domain, role='lkz')

    sidebar.click_button(sidebar.producers_list_button, do_assert=True, wait="lst")

    produser_list = ProdusersList(base.driver)
    produser_list.click_button(produser_list.producer_logo_inn, wait="form")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.add_agreements_button, wait="form")

    add_agr = AgreementAdd(base.driver)
    add_agr.input_in_field(add_agr.agr_number_input, f"№-{base.get_timestamp()}")
    add_agr.click_button(add_agr.agr_add_date_button)
    add_agr.click_button(add_agr.today_button)
    add_agr.click_button(add_agr.agr_end_date_button)
    time.sleep(0.5)
    add_agr.input_in_field(add_agr.agr_date_input, "01012045")
    add_agr.dropdown_click_input_click(add_agr.registers_auto_select, "Автоматическое формирование Реестров отключено")
    add_agr.click_button(add_agr.add_agr_button, do_assert=True)
    add_agr.click_button(add_agr.confirm_add_button, wait="lst")

    sidebar.finish_test()
