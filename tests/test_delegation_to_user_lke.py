import allure
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_test import base_test_with_login
from pages.clients_list_page import ClientsList
from pages.contractor_page import Contractor
from pages.producers_list_page import ProducersList


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКЭ. Тест делегирования пользователю права управления ЛК ГВ: пользователь - Пятый в списке')
def test_delegation_client_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    client_list.click_button(client_list.client_lkz_inn, wait="lst")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.settings_tab)
    contractor.click_button(contractor.user_checkbox_empty, 2)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    contractor.click_button(contractor.user_checkbox_filled, 3)
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКЭ. Тест делегирования пользователю права управления ЛК ПВ: пользователь - Пятый в списке')
def test_delegation_producer_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.click_button(producer_list.producer_lkp_inn, wait="lst")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.settings_tab)
    contractor.click_button(contractor.user_checkbox_empty, 2, wait_type="located")
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    contractor.click_button(contractor.user_checkbox_filled, 3, wait_type="located")
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Делегирование прав управления ЛК')
@allure.description('ЛКЭ. Тест делегирования пользователю управления ЛК внутр.ПВ: пользователь - Пятый в списке')
def test_delegation_inner_producer_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.click_button(producer_list.producer_vaz_inn, wait="lst")

    contractor = Contractor(base.driver)
    contractor.click_button(contractor.settings_tab)
    contractor.click_button(contractor.user_checkbox_empty, 2, wait_type="visible")
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)
    contractor.click_button(contractor.user_checkbox_filled, 3, wait_type="visible")
    contractor.click_button(contractor.save_delegation_button, do_assert=True)
    contractor.click_button(contractor.ok_button)

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Переход в ЛК делигировавшего КА')
@allure.description('ЛКЭ. Тест перехода в ЛК делигировавшего ГВ: гв - auto LKZ')
def test_go_to_account_client_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")

    client_list = ClientsList(base.driver)
    client_list.move_and_click(move_to=client_list.action_button, click_to=client_list.go_to_account_button)

    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    client_list.assert_word(client_list.assert_auto_lkz)

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Переход в ЛК делигировавшего КА')
@allure.description('ЛКЭ. Тест перехода в ЛК делигировавшего ПВ: пв - auto LKP')
def test_go_to_account_producer_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.move_and_click(move_to=producer_list.action_button_lkp, click_to=producer_list.go_to_account_button)

    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    producer_list.assert_word(producer_list.assert_auto_lkp)

    sidebar.test_finish()


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Переход в ЛК делигировавшего КА')
@allure.description('ЛКЭ. Тест перехода в ЛК делигировавшего внутреннего ПВ: пв - НАО АВТОВАЗ')
def test_go_to_account_inner_producer_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')

    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")

    producer_list = ProducersList(base.driver)
    producer_list.move_and_click(move_to=producer_list.action_button_vaz, click_to=producer_list.go_to_account_button)

    WebDriverWait(base.driver, 60).until(lambda d: len(d.window_handles) > 1)
    windows = base.driver.window_handles
    base.driver.switch_to.window(windows[1])
    producer_list.assert_word(producer_list.assert_auto_vaz)

    sidebar.test_finish()
