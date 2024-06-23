import allure
from pages.producers_list_page import ProducersList
from tests.base_test import base_test_with_login
from pages.contractor_page import Contractor


@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКП. Тест делегирования управлением ЛК: кому - Auto LKE, '
                    'тип - перебор всех вариантов с проверкой сохранения')
def test_delegation_to_lke_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
    # Переход к списку перевозчиков
    sidebar.click_button(sidebar.producers_list_button, do_assert=True, wait="lst")
    
    producers_list = ProducersList(base.driver)
    # Клик по перевозчику с ИНН "producer_lke_inn"
    producers_list.click_button(producers_list.producer_lke_inn, wait="form")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек
    contractor.click_button(contractor.settings_tab)
    # Установка делегирования "Нет" и сохранение
    contractor.dropdown_click_input_click(contractor.delegation_type_select, "Нет")
    contractor.click_button(contractor.save_button, do_assert=True)
    # Установка делегирования "Делегировать только управление подбором ТС и водителей" и сохранение
    contractor.dropdown_click_input_click(contractor.delegation_type_select,
                                          "Делегировать только управление подбором ТС и водителей")
    contractor.click_button(contractor.save_button, do_assert=True)
    # Установка делегирования "Да, полное делегирование" и сохранение
    contractor.dropdown_click_input_click(contractor.delegation_type_select, "Да, полное делегирование")
    contractor.click_button(contractor.save_button, do_assert=True)
    
    # Завершение теста
    sidebar.test_finish()
