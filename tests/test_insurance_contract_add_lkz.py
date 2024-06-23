import allure
from tests.base_test import base_test_with_login
from pages.insurance_contract_add_page import InsuranceAdd
from pages.insurer_page import Insurer
from pages.insurers_list_page import InsurersList


@allure.story("Extended test")
@allure.feature('Создание договоров страхования')
@allure.description('ЛКЗ. Тест договора страхования: номер и название - № и Н-timestamp, срок - с Сегодня, '
                    'макс стоимость - 1кккруб, бордеро - Да, премия - 0.05%, мин - 50руб.')
def test_insurance_contract_add_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
    # Переход к списку страховщиков
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    
    insurers_list = InsurersList(base.driver)
    # Клик по страховщику с ИНН "insurer_energy_inn"
    insurers_list.click_button(insurers_list.insurer_energy_inn)
    
    insurer = Insurer(base.driver)
    # Переход на вкладку договоров страховщика
    insurer.click_button(insurer.insurer_contracts, wait="lst")
    # Клик по кнопке добавления договора
    insurer.click_button(insurer.add_contract_button)
    
    add_contract = InsuranceAdd(base.driver)
    # Ввод номера договора
    add_contract.input_in_field(add_contract.number_contract_field, f"№-{base.get_timestamp()}")
    # Ввод названия договора
    add_contract.input_in_field(add_contract.name_contract_field, f"Н-{base.get_timestamp()}")
    # Установка даты подписания договора на сегодня
    add_contract.click_button(add_contract.date_signing_field)
    add_contract.click_button(add_contract.today_button)
    # Ввод максимальной стоимости договора
    add_contract.input_in_field(add_contract.max_value_field, "1000000000")
    # Включение бордеро
    add_contract.click_button(add_contract.bordero_togl)
    # Ввод страховой премии
    add_contract.input_in_field(add_contract.insurance_premium_field, "0.05")
    # Ввод минимальной премии
    add_contract.input_in_field(add_contract.min_premium_field, "50")
    # Клик по кнопке добавления договора
    add_contract.click_button(add_contract.add_contract_button, do_assert=True)
    # Клик по кнопке подтверждения добавления договора
    add_contract.click_button(add_contract.confirm_add_button)
    
    # Завершение теста
    sidebar.test_finish()
