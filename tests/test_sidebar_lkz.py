import allure
from tests.base_test import base_test_with_login


@allure.epic("Стабильные тесты")
@allure.story("Smoke test")
@allure.feature('Боковое меню')
@allure.description('ЛКЗ. Тест бокового меню: переход по всем вкладкам, '
                    'ожидание прогрузки, проверка вкладки по названию')
def test_sidebar_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                                do_assert=True, wait="form")
    sidebar.move_find_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_inter_button,
                                do_assert=True, wait="form")
    sidebar.move_find_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ltl_button,
                                do_assert=True, wait="form")
    sidebar.move_find_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_regular_button,
                                do_assert=True, wait="form")
    sidebar.move_find_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_loaders_button,
                                do_assert=True, wait="form")
    sidebar.move_find_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ltl_active_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_archive_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.order_hover, click_to=sidebar.auction_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.order_hover, click_to=sidebar.regular_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.order_hover, click_to=sidebar.deferred_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.assignments_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.dispatch_list_button,
                                do_assert=True, wait="lst")
    sidebar.click_button(sidebar.producers_list_button, do_assert=True)
    sidebar.click_button(sidebar.registries_list_button_lkz, do_assert=True)
    sidebar.click_button(sidebar.transport_doc_list_button, do_assert=True)
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                                do_assert=True, wait="lst")
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    sidebar.move_find_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_client_button)
    sidebar.switch_to_original_window()
    sidebar.move_find_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_producer_button)
    sidebar.switch_to_original_window()
    sidebar.move_find_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_dispatcher_button)
    sidebar.switch_to_original_window()
    sidebar.move_find_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_app_button)
    sidebar.switch_to_original_window()
    sidebar.move_find_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.faq_button)
    sidebar.switch_to_original_window()
    sidebar.click_button(sidebar.monitor_button, do_assert=True)
    sidebar.click_button(sidebar.exit_button)

    sidebar.finish_test()
