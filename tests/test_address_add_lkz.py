import allure
from tests.base_test import base_test
from pages.address_add_page import AddressAdd
from pages.address_list_page import AddressesList


@allure.feature('Создание адресов')
@allure.description('ЛКЗ. Тест создания адреса: статус - Активный, ввод адреса в поле Фактический адрес.')
def test_address_add_lkz(domain):
    base, sidebar = base_test(domain=domain, role='lkz')
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                                do_assert=True, wait="lst")

    address_list = AddressesList(base.driver)
    address_list.click_button(address_list.add_address_button, wait="form")

    add_address = AddressAdd(base.driver)
    add_address.click_button(add_address.status_toggl)
    add_address.input_in_field(add_address.address_input,
                               f"г Екатеринбург, пр-кт Ленина, д {base.random_value_int_str(1, 150)}")
    add_address.click_button(add_address.create_address_button, do_assert=True)
    add_address.click_button(add_address.confirm_add_button, wait="lst")

    sidebar.finish_test()
