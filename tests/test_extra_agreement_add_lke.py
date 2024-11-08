import allure
import pytest
import time
from pages.agreement_page import Agreement
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd
from pages.producers_list_page import ProducersList


@allure.story("Smoke test")
@allure.feature('Создание ДУ')
@allure.description('ЛКЭ. Тест создания ДУ с ГВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_extra_agreements_client_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку клиентов
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lkz_inn"
    client_list.click_button(client_list.client_lkz_inn, wait="lst")

    contractor = Contractor(base.driver)
    # Переход на вкладку договоров
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке добавления дополнительного соглашения
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    # Заполнение формы дополнительного соглашения
    extra_agr_number = add_extra.add_base_extra_agreements()
    # Клик по кнопке "Назначить позже"
    add_extra.click_button(add_extra.appoint_later_button, do_assert=True)
    # Клик по кнопке подтверждения добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке удаления ДУ
    agreement.click_button(agreement.delete_extra_agr_button)
    # Клик по кнопке подтверждения удаления ДУ
    agreement.click_button(agreement.yes_button, wait="form")
    time.sleep(1.5)
    # Проверка отсутствия удаленного ДУ
    agreement.verify_text_on_page(extra_agr_number, should_exist=False)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание ДУ')
@allure.description('ЛКЭ. Тест создания ДУ с ПВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_extra_agreements_producer_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    # Клик по перевозчику с ИНН "producer_lkp_inn"
    producer_list.click_button(producer_list.producer_lkp_inn, wait="lst")

    contractor = Contractor(base.driver)
    # Переход на вкладку договоров
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке добавления дополнительного соглашения
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    # Заполнение формы дополнительного соглашения
    extra_agr_number = add_extra.add_base_extra_agreements()
    # Клик по кнопке "Назначить позже"
    add_extra.click_button(add_extra.appoint_later_button, do_assert=True)
    # Клик по кнопке подтверждения добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке удаления ДУ
    agreement.click_button(agreement.delete_extra_agr_button)
    # Клик по кнопке подтверждения удаления ДУ
    agreement.click_button(agreement.yes_button, wait="form")
    time.sleep(1.5)
    # Проверка отсутствия удаленного ДУ
    agreement.verify_text_on_page(extra_agr_number, should_exist=False)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание ДУ')
@allure.description('ЛКЭ. Тест создания ДУ с внутр. ПВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_extra_agreements_inner_contractor_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    # Клик по перевозчику с ИНН "producer_vaz_inn"
    producer_list.click_button(producer_list.producer_vaz_inn, wait="lst")

    contractor = Contractor(base.driver)
    # Переход на вкладку договоров
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке добавления дополнительного соглашения
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    # Заполнение формы дополнительного соглашения
    extra_agr_number = add_extra.add_base_extra_agreements()
    # Клик по кнопке "Назначить позже"
    add_extra.click_button(add_extra.appoint_later_button, do_assert=True)
    # Клик по кнопке подтверждения добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке удаления ДУ
    agreement.click_button(agreement.delete_extra_agr_button)
    # Клик по кнопке подтверждения удаления ДУ
    agreement.click_button(agreement.yes_button, wait="form")
    time.sleep(1.5)
    # Проверка отсутствия удаленного ДУ
    agreement.verify_text_on_page(extra_agr_number, should_exist=False)
    # Конец теста
