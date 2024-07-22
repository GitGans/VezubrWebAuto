import allure
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from tests.base_test import base_test_with_login


@allure.story("Smoke test")
@allure.feature('Прикрепление и открепление договоров страхования')
@allure.description('ЛКЭ. Тест прикрепления и открепления договора страхования к ГВ')
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
    # Переход на вкладку настроек контрагента
    contractor.click_button(contractor.settings_tab)
    # Разворачивание списка договоров страхования
    contractor.click_button(contractor.insurance_expandable_list)
    # Выбор страховой компании "Энергогарант"
    contractor.dropdown_click_input_click(contractor.insurance_company_select, "Энергогарант")
    # Выбор конкретного договора страхования
    contractor.dropdown_click_input_click(contractor.insurance_contract_select,
                                          "Договор №№-20240222214909 «Н-20240222214909» от 23.02.2024")
    # Подтверждение привязки договора
    contractor.click_button(contractor.confirm_button, do_assert=True)
    # Подтверждение успешного выполнения действия
    contractor.click_button(contractor.ok_button)
    # Очистка выбора договора страхования для дальнейшего открепления
    contractor.move_and_click(move_to=contractor.insurance_contract_select, click_to=contractor.clear_button)
    # Клик по кнопке открепления договора
    contractor.click_button(contractor.delete_button, do_assert=True)
    # Подтверждение открепления договора
    contractor.click_button(contractor.ok_button)
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Прикрепление и открепление договоров страхования')
@allure.description('ЛКП. Тест прикрепления и открепления договора страхования к ГВ')
def test_insurance_contract_attach_lkp(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkp'
    base, sidebar = base_test_with_login(domain=domain, role='lkp')
    
    # Переход к списку клиентов
    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")
    
    client_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lkz_inn"
    client_list.click_button(client_list.client_lkz_inn, wait="form")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек контрагента
    contractor.click_button(contractor.settings_tab)
    # Разворачивание списка договоров страхования
    contractor.click_button(contractor.insurance_expandable_list)
    # Выбор страховой компании "Энергогарант"
    contractor.dropdown_click_input_click(contractor.insurance_company_select, "Энергогарант")
    # Выбор конкретного договора страхования
    contractor.dropdown_click_input_click(contractor.insurance_contract_select,
                                          "Договор №№-20240222215011 «Н-20240222215011» от 23.02.2024")
    # Подтверждение привязки договора
    contractor.click_button(contractor.confirm_button, do_assert=True)
    # Подтверждение успешного выполнения действия
    contractor.click_button(contractor.ok_button)
    # Очистка выбора договора страхования для дальнейшего открепления
    contractor.move_and_click(move_to=contractor.insurance_contract_select, click_to=contractor.clear_button)
    # Клик по кнопке открепления договора
    contractor.click_button(contractor.delete_button, do_assert=True)
    # Подтверждение открепления договора
    contractor.click_button(contractor.ok_button)
    
    # Завершение теста
    sidebar.test_finish()
    