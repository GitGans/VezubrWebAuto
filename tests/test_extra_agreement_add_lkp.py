import allure
from tests.base_test import base_test_with_login
from pages.agreement_page import Agreement
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd


@allure.feature('Создание ДУ')
@allure.description('ЛКП. Тест создания ДУ с ГВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
def test_extra_agreements_client_add_lkp(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkp')

    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    client_list.click_button(client_list.client_lkz_inn, wait="lst")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    agreement.click_button(agreement.extra_agreement_tab)
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    add_extra.add_base_extra_agreements()
    add_extra.click_button(add_extra.appoint_later_button, do_assert=True)
    add_extra.click_button(add_extra.confirm_add_button, wait="form")

    sidebar.finish_test()
