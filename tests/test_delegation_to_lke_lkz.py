import allure
from pages.producers_list_page import ProducersList
from tests.base_test import base_test_with_login
from pages.contractor_page import Contractor


@allure.feature('Создание договоров')
@allure.description('ЛКП. Тест делегирования управлением ЛК: кому - Auto LKE, '
                    'тип - перебор всех вариантов с проверкой сохранения')
def test_delegation_to_lke_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.click_button(sidebar.producers_list_button, do_assert=True, wait="lst")

    producers_list = ProducersList(base.driver)
    producers_list.click_button(producers_list.producer_lke_inn, wait="form")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.settings_tab)
    contractor.dropdown_click_input_click(contractor.delegation_type_select, "Нет")
    contractor.click_button(contractor.save_button, do_assert=True)
    contractor.dropdown_click_input_click(contractor.delegation_type_select,
                                           "Делегировать только управление подбором ТС и водителей")
    contractor.click_button(contractor.save_button, do_assert=True)
    contractor.dropdown_click_input_click(contractor.delegation_type_select, "Да, полное делегирование")
    contractor.click_button(contractor.save_button, do_assert=True)

    sidebar.finish_test()
