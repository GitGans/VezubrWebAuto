import allure
from tests.base_test import base_test_with_login
from pages.insurance_contract_add_page import InsuranceAdd
from pages.insurer_page import Insurer
from pages.insurers_list_page import InsurersList


@allure.feature('Создание договоров страхования')
@allure.description('ЛКЗ. Тест договора страхования: номер и название - № и Н-timestamp, срок - с Сегодня, '
                    'макс стоимость - 1кккруб, бордеро - Да, премия - 0.05%, мин - 50руб.')
def test_insurance_contract_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                                do_assert=True, wait="lst")

    insurers_list = InsurersList(base.driver)
    insurers_list.click_button(insurers_list.insurer_energy_inn)

    insurer = Insurer(base.driver)
    insurer.click_button(insurer.insurer_contracts, wait="lst")
    insurer.click_button(insurer.add_contract_button)

    add_contract = InsuranceAdd(base.driver)
    add_contract.input_in_field(add_contract.number_contract_field, f"№-{base.get_timestamp()}")
    add_contract.input_in_field(add_contract.name_contract_field, f"Н-{base.get_timestamp()}")
    add_contract.click_button(add_contract.date_signing_field)
    add_contract.click_button(add_contract.today_button)
    add_contract.input_in_field(add_contract.max_value_field, "1000000000")
    add_contract.click_button(add_contract.bordero_togl)
    add_contract.input_in_field(add_contract.insurance_premium_field, "0.05")
    add_contract.input_in_field(add_contract.min_premium_field, "50")
    add_contract.click_button(add_contract.add_contract_button, do_assert=True)
    add_contract.click_button(add_contract.confirm_add_button, wait="lst")

    sidebar.finish_test()
