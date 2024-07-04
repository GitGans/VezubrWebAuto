import allure
from pages.clients_list_page import ClientsList
from tests.base_test import base_test_with_login
from pages.agreement_page import Agreement
from pages.contractor_page import Contractor
from pages.extra_agreement_add_page import ExtraAgreementAdd


@allure.feature('Прикрепление тарифов')
@allure.story("Critical path test")
@allure.description('ЛКП. Тест прикрепления тарифа к ДУ c ГВ: создаем базовый ДУ и сразу прикрепляем существующий '
                    'тариф - Первый в списке')
def test_tariff_attach_client_lkp(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkp'
    base, sidebar = base_test_with_login(domain=domain, role='lkp')

    # Переход к списку клиентов
    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")

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

    # Завершение теста
    sidebar.test_finish()
