import time
import allure
from tests.base_test import base_test_with_login
from pages.request_ftl_add_page import FTLAdd


@allure.feature('Создание FTL заявок')
@allure.description('ЛКЗ. Тест создания FTL заявки: тип - Город, подача - Сейчас, ТС - Груз 0.5т, '
                    'кузов - Закрытый, адреса - Первые в списке, публикация - Тариф')
def test_ftl_request_add_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                                do_assert=True, wait="form")

    ftl = FTLAdd(base.driver)
    ftl.click_button(ftl.start_date_field)
    ftl.click_button(ftl.today_button)
    ftl.click_button(ftl.start_time_field)
    new_time = ftl.naw_time_change(30)
    ftl.input_in_field(ftl.start_time_input, new_time)
    time.sleep(1)
    ftl.click_button(ftl.request_category_select)
    ftl.click_button(ftl.select_freight)
    ftl.click_button(ftl.vehicle_type_select)
    ftl.dropdown_click_input_click(ftl.vehicle_type_select, "до 0.5т")
    ftl.click_button(ftl.vehicle_body_select)
    ftl.click_button(ftl.body_type_closed_checkbox)
    ftl.click_button(ftl.first_address_select, wait="lst")
    ftl.click_button(ftl.select_first_radio)
    ftl.click_button(ftl.confirm_address_button)
    time.sleep(2)
    ftl.click_button(ftl.second_address_select, wait="lst")
    ftl.click_button(ftl.select_second_radio)
    ftl.click_button(ftl.confirm_address_button)
    ftl.get_element_clickable(ftl.calculate_finish)
    ftl.click_button(ftl.tariff_button)
    ftl.click_button(ftl.producer_select)
    ftl.click_button(ftl.select_all_producer)
    ftl.click_button(ftl.producer_select_text)
    ftl.click_button(ftl.publish_button)
    ftl.click_button(ftl.continue_button, do_assert=True)
    ftl.click_button(ftl.confirm_add_button, wait="lst")

    sidebar.finish_test()
