import allure
import pytest
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor


@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКП. Тест делегирования управлением ЛК: кому - Auto LKE, '
                    'тип - перебор всех вариантов с проверкой сохранения')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_delegation_to_lke_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку клиентов
    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")
    
    clients_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lke_inn"
    clients_list.click_button(clients_list.client_lke_inn, wait="form")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек
    contractor.click_button(contractor.settings_tab)
    # Установка делегирования "Нет" и сохранение
    contractor.dropdown_without_input(contractor.delegation_type_select, "Нет")
    contractor.click_button(contractor.save_button, do_assert=True)
    # Установка делегирования "Делегировать только управление подбором ТС и водителей" и сохранение
    contractor.dropdown_without_input(contractor.delegation_type_select,
                                          "Делегировать только управление подбором ТС и водителей")
    contractor.click_button(contractor.save_button, do_assert=True)
    # Установка делегирования "Да, полное делегирование" и сохранение
    contractor.dropdown_without_input(contractor.delegation_type_select, "Да, полное делегирование")
    contractor.click_button(contractor.save_button, do_assert=True)
    # Конец теста
