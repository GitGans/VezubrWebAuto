import time
import allure
from tests.base_test import base_test
from pages.agreement_add_page import AgreementAdd
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor


@allure.feature('Создание договоров')
@allure.description('ЛКП. Тест создания договора с ГВ: '
                    'номер - №-timestamp, срок - с Сегодня по 45 год, автоформирование реестров - Отключено.')
def test_agreement_client_add_lkp(domain):
    base, sidebar = base_test(domain=domain, role='lkp')

    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    client_list.click_button(client_list.client_lkz_inn, wait="form")

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
