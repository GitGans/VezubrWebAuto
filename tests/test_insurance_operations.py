import allure
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from tests.base_test import base_test_with_login


@allure.story("Smoke test")
@allure.feature('Привкрепление и открепление договоров страхования')
@allure.description('ЛКЭ. Тест привкрепления и открепления договора страхования к ГВ')
def test_insurance_contract_attach_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку клиентов
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    
    client_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lkz_inn"
    client_list.click_button(client_list.client_lkz_inn, wait="form")
    
    contractor = Contractor(base.driver)
    contractor.click_button(contractor.settings_tab)
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Привкрепление и открепление договоров страхования')
@allure.description('ЛКП. Тест привкрепления и открепления договора страхования к ГВ')
def test_insurance_contract_attach_lkp(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkp'
    base, sidebar = base_test_with_login(domain=domain, role='lkp')
    
    

    # Завершение теста
    sidebar.test_finish()
