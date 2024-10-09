import allure
import pytest
from pages.agreement_page import Agreement
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd
from pages.producers_list_page import ProducersList


@allure.feature('Прикрепление тарифов')
@allure.story("Smoke test")
@allure.description('ЛКЭ. Тест прикрепления тарифа к ДУ c ГВ: создаем базовый ДУ и сразу прикрепляем существующий '
                    'тариф - Первый в списке')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tariff_attach_client_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку клиентов
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    # Выбор клиента по ИНН
    client_list.click_button(client_list.client_lkz_inn, wait="lst")

    contractor = Contractor(base.driver)
    # Переход к договорам
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке добавления дополнительного соглашения
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    # Создание базового дополнительного соглашения
    add_extra.add_base_extra_agreements()
    # Выбор тарифа
    add_extra.click_button(add_extra.radio_button, wait_type="located")
    # Подтверждение выбора тарифа
    add_extra.click_button(add_extra.confirm_tariff_button, do_assert=True)
    # Подтверждение добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    # Конец теста


@allure.feature('Прикрепление тарифов')
@allure.story("Smoke test")
@allure.description('ЛКЭ. Тест прикрепления тарифа к ДУ c ПВ: создаем базовый ДУ и сразу прикрепляем существующий '
                    'тариф - Первый в списке')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tariff_attach_producer_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    # Выбор перевозчика по ИНН
    producer_list.click_button(producer_list.producer_lkp_inn, wait="lst")

    contractor = Contractor(base.driver)
    # Переход к договорам
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке добавления дополнительного соглашения
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    # Создание базового дополнительного соглашения
    add_extra.add_base_extra_agreements()
    # Выбор тарифа
    add_extra.click_button(add_extra.radio_button, wait_type="located")
    # Подтверждение выбора тарифа
    add_extra.click_button(add_extra.confirm_tariff_button, do_assert=True)
    # Подтверждение добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    # Конец теста


@allure.feature('Прикрепление тарифов')
@allure.story("Smoke test")
@allure.description('ЛКЭ. Тест прикрепления тарифа к ДУ внутр. ПВ: создаем базовый ДУ и сразу прикрепляем существующий'
                    ' тариф - Первый в списке')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_tariff_attach_inner_producer_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    # Выбор внутреннего перевозчика по ИНН
    producer_list.click_button(producer_list.producer_vaz_inn, wait="lst")

    contractor = Contractor(base.driver)
    # Переход к договорам
    contractor.click_button(contractor.agreements_link, wait="form")

    agreement = Agreement(base.driver)
    # Переход на вкладку дополнительных соглашений
    agreement.click_button(agreement.extra_agreement_tab)
    # Клик по кнопке добавления дополнительного соглашения
    agreement.click_button(agreement.add_extra_agr_button)

    add_extra = ExtraAgreementAdd(base.driver)
    # Создание базового дополнительного соглашения
    add_extra.add_base_extra_agreements()
    # Выбор тарифа
    add_extra.click_button(add_extra.radio_button, wait_type="located")
    # Подтверждение выбора тарифа
    add_extra.click_button(add_extra.confirm_tariff_button, do_assert=True)
    # Подтверждение добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    # Конец теста
