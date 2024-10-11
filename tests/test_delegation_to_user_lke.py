import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from pages.producers_list_page import ProducersList


@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКЭ. Тест делегирования пользователю права управления ЛК ГВ: '
                    'делегируем - Второму, отменяем - Третьему')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_delegation_client_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку клиентов
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    
    client_list = ClientsList(base.driver)
    # Клик по клиенту с ИНН "client_lkz_inn"
    client_list.click_button(client_list.client_lkz_inn, wait="lst")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек
    contractor.click_button(contractor.settings_tab)
    # Делегирование пользователю (1-й в списке не выбранный) права управления ЛК
    contractor.click_button(contractor.user_checkbox_empty, 1)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    # Отмена делегирования пользователю (4-й в списке)
    contractor.click_button(contractor.user_checkbox_filled, 4)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКЭ. Тест делегирования пользователю права управления ЛК ГВ: '
                    'делегируем - Второму, отменяем - Третьему')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_delegation_producer_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Клик по перевозчику с ИНН "producer_lkp_inn"
    producer_list.click_button(producer_list.producer_lkp_inn, wait="lst")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек
    contractor.click_button(contractor.settings_tab)
    # Делегирование пользователю (1-й в списке не выбранный) права управления ЛК
    contractor.click_button(contractor.user_checkbox_empty, 1)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    # Отмена делегирования пользователю (4-й в списке)
    contractor.click_button(contractor.user_checkbox_filled, 4)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКЭ. Тест делегирования пользователю права управления ЛК ГВ: '
                    'делегируем - Второму, отменяем - Третьему')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_delegation_inner_producer_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Клик по перевозчику с ИНН "producer_vaz_inn"
    producer_list.click_button(producer_list.producer_vaz_inn, wait="lst")
    
    contractor = Contractor(base.driver)
    # Переход на вкладку настроек
    contractor.click_button(contractor.settings_tab)
    # Делегирование пользователю (1-й в списке не выбранный) права управления ЛК
    contractor.click_button(contractor.user_checkbox_empty, 1)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    # Отмена делегирования пользователю (4-й в списке)
    contractor.click_button(contractor.user_checkbox_filled, 4)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Переход в ЛК делегировавшего КА')
@allure.description('ЛКЭ. Тест перехода в ЛК делегировавшего ГВ: гв - auto LKZ')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_go_to_account_client_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку клиентов
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    
    client_list = ClientsList(base.driver)
    # Переход в ЛК клиента
    client_list.move_and_click(move_to=client_list.action_button, click_to=client_list.go_to_account_button)
    
    # Ожидание открытия новой вкладки и переключение на нее
    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    # Проверка корректности перехода в ЛК клиента
    client_list.assert_element_text(client_list.assert_auto_lkz)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Переход в ЛК делегировавшего КА')
@allure.description('ЛКЭ. Тест перехода в ЛК делегировавшего ПВ: пв - auto LKP')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_go_to_account_producer_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход к списку перевозчиков
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    
    producer_list = ProducersList(base.driver)
    # Переход в ЛК перевозчика
    producer_list.move_and_click(move_to=producer_list.action_button_lkp, click_to=producer_list.go_to_account_button)
    
    # Ожидание открытия новой вкладки и переключение на нее
    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    # Проверка корректности перехода в ЛК перевозчика
    producer_list.assert_element_text(producer_list.assert_auto_lkp)
    # Конец теста
