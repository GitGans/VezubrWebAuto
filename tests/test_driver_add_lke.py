import allure
from tests.base_test import base_test
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList


@allure.feature('Создание водителей')
@allure.description('ЛКЭ. Тест создания водителя Экс: '
                    'ФИО - ФИО-timestamp, паспорт/права - РФ,  № паспорт/код/права/тлф.апп/тлф. - Рандом.')
def test_own_driver_add_lke(domain):
    base, sidebar = base_test(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                                do_assert=True, wait="lst")

    driver_list = DriverList(base.driver)
    driver_list.click_button(driver_list.add_driver_button, wait="form")

    add_driver = DriverAdd(base.driver)
    add_driver.add_base_driver()

    sidebar.finish_test()


@allure.feature('Создание водителей')
@allure.description('ЛКЭ. Тест создания водителя внутр КА: ка - Первыйй в списке, ФИО - ФИО-timestamp, '
                    'паспорт/права - РФ,  № паспорт/код/права/тлф. - Рандом.')
def test_inner_driver_add_lke(domain):
    base, sidebar = base_test(domain=domain, role='lke')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                                do_assert=True, wait="lst")

    driver_list = DriverList(base.driver)
    driver_list.click_button(driver_list.add_driver_button, wait="form")

    add_driver = DriverAdd(base.driver)
    add_driver.add_base_inner_driver()

    sidebar.finish_test()
