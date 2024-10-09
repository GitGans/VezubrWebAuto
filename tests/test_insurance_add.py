import allure
import pytest
from pages.insurance_contract_add_page import InsuranceAdd
from pages.insurer_page import Insurer
from pages.insurers_list_page import InsurersList


@allure.story("Smoke test")
@allure.feature('Создание и завершение договоров страхования')
@allure.description('ЛКЭ. Тест создания договора страхования: номер и название - № и Н-timestamp, срок - с Сегодня, '
                    'макс стоимость - 1ккк, бордеро - Да, премия - 0.05%, мин - 50руб, в конце - Удаляем')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_insurance_contract_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
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
    add_contract.click_button(add_contract.confirm_button)
    
    # Переход к списку страховщиков
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    
    # Клик по страховщику с ИНН "insurer_energy_inn"
    insurers_list.click_button(insurers_list.insurer_energy_inn)
    
    # Переход на вкладку договоров страховщика
    insurer.click_button(insurer.insurer_contracts, wait="lst")
    # Клик по первой ссылке договора в списке
    insurer.click_button(insurer.first_contract_link)
    
    # Открытие меню действий и закрытие договора
    add_contract.click_button(add_contract.action_menu_button)
    add_contract.click_button(add_contract.close_contract_button)
    # Подтверждение закрытия договора
    add_contract.click_button(add_contract.confirm_button, do_assert=True)
    add_contract.click_button(add_contract.confirm_button)
    # Конец теста


@allure.story("Smoke test")
@allure.feature('Создание и завершение договоров страхования')
@allure.description('ЛКП. Тест создания договора страхования: номер и название - № и Н-timestamp, срок - с Сегодня, '
                    'макс стоимость - 1ккк, бордеро - Да, премия - 0.05%, мин - 50руб, в конце - Удаляем')
@pytest.mark.parametrize('base_fixture', ['lkp'], indirect=True)  # Параметризация роли
def test_insurance_contract_add_lkp(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
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
    add_contract.click_button(add_contract.confirm_button)
    # Переход к списку страховщиков
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    
    # Клик по страховщику с ИНН "insurer_energy_inn"
    insurers_list.click_button(insurers_list.insurer_energy_inn)
    
    # Переход на вкладку договоров страховщика
    insurer.click_button(insurer.insurer_contracts, wait="lst")
    # Клик по первой ссылке договора в списке
    insurer.click_button(insurer.first_contract_link)
    
    # Открытие меню действий и закрытие договора
    add_contract.click_button(add_contract.action_menu_button)
    add_contract.click_button(add_contract.close_contract_button)
    # Подтверждение закрытия договора
    add_contract.click_button(add_contract.confirm_button, do_assert=True)
    add_contract.click_button(add_contract.confirm_button)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Создание и завершение договоров страхования')
@allure.description('ЛКЗ. Тест создания договора страхования: номер и название - № и Н-timestamp, срок - с Сегодня, '
                    'макс стоимость - 1ккк, бордеро - Да, премия - 0.05%, мин - 50руб, в конце - Удаляем')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_insurance_contract_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
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
    add_contract.click_button(add_contract.confirm_button)
    
    # Переход к списку страховщиков
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    
    # Клик по страховщику с ИНН "insurer_energy_inn"
    insurers_list.click_button(insurers_list.insurer_energy_inn)
    
    # Переход на вкладку договоров страховщика
    insurer.click_button(insurer.insurer_contracts, wait="lst")
    # Клик по первой ссылке договора в списке
    insurer.click_button(insurer.first_contract_link)
    
    # Открытие меню действий и закрытие договора
    add_contract.click_button(add_contract.action_menu_button)
    add_contract.click_button(add_contract.close_contract_button)
    # Подтверждение закрытия договора
    add_contract.click_button(add_contract.confirm_button, do_assert=True)
    add_contract.click_button(add_contract.confirm_button)
    # Конец теста
