import allure
from tests.base_test import base_test
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList


@allure.feature('Создание водителей')
@allure.description('ЛКП. Тест создания водителя Экс: '
                    'ФИО - ФИО-timestamp, паспорт/права - РФ,  № паспорт/код/права/тлф.апп/тлф. - Рандом.')
def test_driver_add_lkp(domain):
    base, sidebar = base_test(domain=domain, role='lkp')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                                do_assert=True, wait="lst")

    driver_list = DriverList(base.driver)
    driver_list.click_button(driver_list.add_driver_button, wait="form")

    add_driver = DriverAdd(base.driver)
    add_driver.add_base_driver()

    sidebar.finish_test()
