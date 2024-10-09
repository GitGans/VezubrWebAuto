import allure
import pytest
from pages.agreement_page import Agreement
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd


@allure.story("Critical path test")
@allure.feature('Создание ДУ')
@allure.description('ЛКП. Тест создания ДУ с ГВ: номер - №-timestamp, срок - с Сегодня по 40 год, '
                    'коммент - ДУ создано автотестом')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_extra_agreements_client_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку клиентов
    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")
    
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
    add_extra.add_base_extra_agreements()
    # Клик по кнопке "Назначить позже"
    add_extra.click_button(add_extra.appoint_later_button, do_assert=True)
    # Клик по кнопке подтверждения добавления дополнительного соглашения
    add_extra.click_button(add_extra.confirm_add_button, wait="form")
    # Конец теста
