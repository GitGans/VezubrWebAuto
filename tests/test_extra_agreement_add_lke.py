import allure
from tests.base_test import base_test_with_login
from pages.agreement_page import Agreement
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd
from pages.producers_list_page import ProducersList


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание ДУ')
@allure.description('ЛКЭ. Тест создания ДУ с ГВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
def test_extra_agreements_client_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")

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

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание ДУ')
@allure.description('ЛКЭ. Тест создания ДУ с ПВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
def test_extra_agreements_producer_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.click_button(producer_list.producer_lkp_inn, wait="lst")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    agreement.click_button(agreement.extra_agreement_tab)
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    add_extra.add_base_extra_agreements()
    add_extra.click_button(add_extra.appoint_later_button, do_assert=True)
    add_extra.click_button(add_extra.confirm_add_button, wait="form")

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание ДУ')
@allure.description('ЛКЭ. Тест создания ДУ с внутр. ПВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
def test_extra_agreements_inner_contractor_add_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.click_button(producer_list.producer_vaz_inn, wait="lst")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    agreement.click_button(agreement.extra_agreement_tab)
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    add_extra.add_base_extra_agreements()
    add_extra.click_button(add_extra.appoint_later_button, do_assert=True)
    add_extra.click_button(add_extra.confirm_add_button, wait="form")

    sidebar.test_finish()
