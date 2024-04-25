import time
import allure
from tests.base_test import base_test_with_login
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Создание грузомест')
@allure.description('ЛКЗ. Тест создания ГМ: '
                    'тип - Короб, вес/объем/цена - Рандом, статус - Новое, адреса - Первые из списка.')
def test_cargo_place_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.assignments_list_button,
                                do_assert=True, wait="lst")
    time.sleep(1)

    cp_list = CargoPlaceList(base.driver)
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")

    add_cp = CargoPlaceAdd(base.driver)
    add_cp.add_base_cargo_place()

    sidebar.finish_test()
