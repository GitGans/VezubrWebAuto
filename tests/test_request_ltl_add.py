import time
import allure
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList
from pages.request_delivery_add_page import DeliveryAdd
from tests.base_test import base_test_with_login


# @allure.story("Smoke test")
# @allure.feature('Создание LTL заявок')
# @allure.description('ЛКЗ. Тест создания LTL заявки: дата - Сейчас +30мин, гм - Первое в списке, публикация - Позже')
# def test_ltl_request_no_publish_add_lkz(domain):
#     # Инициализация базовых объектов и авторизация под ролью 'lkz'
#     base, sidebar = base_test_with_login(domain=domain, role='lkz')
#
#     # Переход к списку грузомест
#     sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
#                            do_assert=True, wait="lst")
#     time.sleep(1)
#
#     cp_list = CargoPlaceList(base.driver)
#     # Клик по кнопке добавления грузоместа
#     cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
#
#     add_cp = CargoPlaceAdd(base.driver)
#     # Добавление базового грузоместа
#     add_cp.add_base_cargo_place_lkz()
#
#     # Переход к созданию новой LTL заявки
#     sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
#                            do_assert=True, wait="form")
#
#     ltl = DeliveryAdd(base.driver)
#     # Выбор типа заявки - Доставка ГМ (LTL)
#     ltl.dropdown_click_input_click(ltl.request_type_select, "Доставку ГМ (LTL)")
#     # Заполнение базовой информации для LTL заявки
#     ltl.add_base_ltl()
#     # Прикрепление грузоместа
#     ltl.click_button(ltl.attach_cargo_place_button)
#     ltl.click_button(ltl.existing_cargo_place_button)
#
#     cpl = CargoPlaceList(base.driver)
#     # Выбор второго грузоместа из списка
#     cpl.click_button(cpl.cp_list_checkbox, 2)
#     cpl.click_button(cpl.confirm_button)
#     time.sleep(1)
#
#     # Клик по кнопке создания заявки
#     ltl.click_button(ltl.create_button)
#     time.sleep(1)
#     # Публикация заявки позже
#     ltl.click_button(ltl.publish_later_button, do_assert=True)
#
#     # Завершение теста
#     sidebar.test_finish()
#
#
# @allure.story("Smoke test")
# @allure.feature('Создание LTL заявок')
# @allure.description('ЛКЗ. Тест создания LTL заявки: дата - Сейчас +30мин, гм - Первое в списке, публикация - Ставка, '
#                     'стоимость - Рандом')
# def test_ltl_request_rate_add_lkz(domain):
#     # Инициализация базовых объектов и авторизация под ролью 'lkz'
#     base, sidebar = base_test_with_login(domain=domain, role='lkz')
#
#     # Переход к списку грузомест
#     sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
#                            do_assert=True, wait="lst")
#     time.sleep(1)
#
#     cp_list = CargoPlaceList(base.driver)
#     # Клик по кнопке добавления грузоместа
#     cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
#
#     add_cp = CargoPlaceAdd(base.driver)
#     # Добавление базового грузоместа
#     add_cp.add_base_cargo_place_lkz()
#
#     # Переход к созданию новой LTL заявки
#     sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
#                            do_assert=True, wait="form")
#
#     ltl = DeliveryAdd(base.driver)
#     # Выбор типа заявки - Доставка ГМ (LTL)
#     ltl.dropdown_click_input_click(ltl.request_type_select, "Доставку ГМ (LTL)")
#     # Прикрепление грузоместа
#     ltl.click_button(ltl.attach_cargo_place_button)
#     ltl.click_button(ltl.existing_cargo_place_button)
#
#     cpl = CargoPlaceList(base.driver)
#     # Выбор второго грузоместа из списка
#     cpl.click_button(cpl.cp_list_checkbox, 2)
#     cpl.click_button(cpl.confirm_button)
#     time.sleep(1)
#
#     # Заполнение базовой информации для LTL заявки
#     ltl.add_base_ltl()
#     # Клик по кнопке создания заявки
#     ltl.click_button(ltl.create_button)
#     time.sleep(1)
#     # Публикация заявки сейчас
#     ltl.click_button(ltl.publish_naw_button, wait="form")
#     # Выбор публикации по ставке
#     ltl.click_button(ltl.tariff_button, wait="form")
#     time.sleep(1)
#     ltl.click_button(ltl.rate_radio)
#     ltl.click_button(ltl.producer_select)
#     ltl.click_button(ltl.producer_button)
#     # Ввод случайной стоимости ставки
#     ltl.input_in_field(ltl.rate_input, base.random_value_float_str(1000, 100000), click_first=True)
#     # Публикация заявки
#     ltl.click_button(ltl.publish_button, do_assert=True)
#     ltl.click_button(ltl.ok_button, wait="lst")
#
#     # Завершение теста
#     sidebar.test_finish()
#
#
# @allure.story("Smoke test")
# @allure.feature('Создание LTL заявок')
# @allure.description('ЛКЗ. Тест создания LTL заявки: дата - Сейчас +30мин, гм - Первое в списке, публикация - Тариф')
# def test_ltl_request_tariff_add_lkz(domain):
#     # Инициализация базовых объектов и авторизация под ролью 'lkz'
#     base, sidebar = base_test_with_login(domain=domain, role='lkz')
#
#     # Переход к списку грузомест
#     sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
#                            do_assert=True, wait="lst")
#     time.sleep(1)
#
#     cp_list = CargoPlaceList(base.driver)
#     # Клик по кнопке добавления грузоместа
#     cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
#
#     add_cp = CargoPlaceAdd(base.driver)
#     # Добавление базового грузоместа
#     add_cp.add_base_cargo_place_lkz()
#
#     # Переход к созданию новой LTL заявки
#     sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_delivery_request_button,
#                            do_assert=True, wait="form")
#
#     ltl = DeliveryAdd(base.driver)
#     # Выбор типа заявки - Доставка ГМ (LTL)
#     ltl.dropdown_click_input_click(ltl.request_type_select, "Доставку ГМ (LTL)")
#     # Прикрепление грузоместа
#     ltl.click_button(ltl.attach_cargo_place_button)
#     ltl.click_button(ltl.existing_cargo_place_button)
#
#     cpl = CargoPlaceList(base.driver)
#     # Выбор второго грузоместа из списка
#     cpl.click_button(cpl.cp_list_checkbox, 2)
#     cpl.click_button(cpl.confirm_button)
#     time.sleep(1)
#
#     # Заполнение базовой информации для LTL заявки
#     ltl.add_base_ltl()
#     # Клик по кнопке создания заявки
#     ltl.click_button(ltl.create_button)
#     time.sleep(1)
#     # Публикация заявки сейчас
#     ltl.click_button(ltl.publish_naw_button, wait="form")
#     # Публикация по тарифу
#     ltl.click_button(ltl.tariff_button, wait="form")
#     time.sleep(1)
#     ltl.click_button(ltl.producer_select)
#     ltl.click_button(ltl.producer_lkp_button)
#     ltl.click_button(ltl.text_to_click)
#     ltl.click_button(ltl.publish_button, do_assert=True)
#     ltl.click_button(ltl.ok_button, wait="lst")
#
#     # Завершение теста
#     sidebar.test_finish()
