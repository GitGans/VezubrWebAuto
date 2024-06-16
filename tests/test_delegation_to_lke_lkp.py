import allure
from tests.base_test import base_test_with_login
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКП. Тест делегирования управлением ЛК: кому - Auto LKE, '
                    'тип - перебор всех вариантов с проверкой сохранения')
def test_delegation_to_lke_lkp(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkp')

    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")

    clients_list = ClientsList(base.driver)
    clients_list.click_button(clients_list.client_lke_inn, wait="form")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.settings_tab)
    contractor.dropdown_click_input_click(contractor.delegation_type_select, "Нет")
    contractor.click_button(contractor.save_button, do_assert=True)
    contractor.dropdown_click_input_click(contractor.delegation_type_select,
                                           "Делегировать только управление подбором ТС и водителей")
    contractor.click_button(contractor.save_button, do_assert=True)
    contractor.dropdown_click_input_click(contractor.delegation_type_select, "Да, полное делегирование")
    contractor.click_button(contractor.save_button, do_assert=True)

    sidebar.test_finish()
