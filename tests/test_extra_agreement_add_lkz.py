import allure
from tests.base_test import base_test_with_login
from pages.agreement_page import Agreement
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd
from pages.producers_list_page import ProducersList


@allure.feature('Создание ДУ')
@allure.description('ЛКЗ. Тест создания ДУ с ПВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
def test_extra_agreements_producer_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.click_button(sidebar.producers_list_button, do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.click_button(producer_list.producer_logo_inn, wait="lst")

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
