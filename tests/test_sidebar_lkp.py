import allure
from tests.base_test import base_test


@allure.feature('Боковое меню')
@allure.description('ЛКП. Тест бокового меню: '
                    'переход по всем вкладкам, ожидание прогрузки, проверка вкладки по названию')
def test_sidebar_lkp(domain):
    base, sidebar = base_test(domain=domain, role='lkp')

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
    sidebar.click_button(sidebar.dispatch_list_button, do_assert=True)
    sidebar.click_button(sidebar.clients_list_button, do_assert=True)
    sidebar.move_find_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_list_button_lkp,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.documents_hover, click_to=sidebar.verification_doc_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                                do_assert=True, wait="lst")
    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
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
