import allure
from tests.base_test import base_test_with_login


@allure.story("Smoke test")
@allure.feature('Боковое меню')
@allure.description('ЛКЭ. Тест бокового меню: переход по всем вкладкам, ожидание прогрузки, '
                    'проверка вкладки по названию')
def test_sidebar_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход по всем вкладкам бокового меню и ожидание их прогрузки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_inter_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ltl_button,
                           do_assert=True, wait="form")
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_regular_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_loaders_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ltl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_archive_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.auction_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.dispatch_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.clients_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.contractor_hover, click_to=sidebar.producers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_producer_create_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_client_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_producer_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.verification_doc_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_client_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_producer_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_dispatcher_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_app_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.faq_button)
    sidebar.switch_to_original_window()
    sidebar.click_button(sidebar.monitor_button, do_assert=True)
    sidebar.click_button(sidebar.exit_button)
    
    # Завершение теста
    sidebar.test_finish()
    
    
@allure.story("Smoke test")
@allure.feature('Боковое меню')
@allure.description('ЛКП. Тест бокового меню: '
                    'переход по всем вкладкам, ожидание прогрузки, проверка вкладки по названию')
def test_sidebar_lkp(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkp'
    base, sidebar = base_test_with_login(domain=domain, role='lkp')
    
    # Переход по всем вкладкам бокового меню и ожидание их прогрузки
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ltl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_archive_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.auction_list_button,
                           do_assert=True, wait="lst")
    sidebar.click_button(sidebar.dispatch_list_button, do_assert=True, wait="lst")
    sidebar.click_button(sidebar.clients_list_button, do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.reg_client_create_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.registries_hover, click_to=sidebar.registries_list_button_lkp,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.transport_doc_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.documents_hover, click_to=sidebar.verification_doc_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.transports_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tractors_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.trailers_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_client_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_producer_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_dispatcher_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_app_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.faq_button)
    sidebar.switch_to_original_window()
    sidebar.click_button(sidebar.monitor_button, do_assert=True)
    sidebar.click_button(sidebar.exit_button)
    
    # Завершение теста
    sidebar.test_finish()
    
    
@allure.story("Smoke test")
@allure.feature('Боковое меню')
@allure.description('ЛКЗ. Тест бокового меню: переход по всем вкладкам, '
                    'ожидание прогрузки, проверка вкладки по названию')
def test_sidebar_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
    # Переход по всем вкладкам бокового меню и ожидание их прогрузки
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_city_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_inter_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ltl_button,
                           do_assert=True, wait="form")
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_ftl_regular_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.new_order_hover, click_to=sidebar.new_loaders_button,
                           do_assert=True)
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ltl_active_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_archive_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.ftl_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.auction_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.regular_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.order_hover, click_to=sidebar.deferred_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.dispatch_list_button,
                           do_assert=True, wait="lst")
    sidebar.click_button(sidebar.producers_list_button, do_assert=True, wait="lst")
    sidebar.click_button(sidebar.registries_list_button_lkz, do_assert=True, wait="lst")
    sidebar.click_button(sidebar.transport_doc_list_button, do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.addresses_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.insurers_list_button,
                           do_assert=True, wait="lst")
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    sidebar.click_button(sidebar.settings_button, do_assert=True)
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_client_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_producer_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_dispatcher_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.instructions_app_button)
    sidebar.switch_to_original_window()
    sidebar.move_and_click(move_to=sidebar.instructions_hover, click_to=sidebar.faq_button)
    sidebar.switch_to_original_window()
    sidebar.click_button(sidebar.monitor_button, do_assert=True)
    sidebar.click_button(sidebar.exit_button)
    
    # Завершение теста
    sidebar.test_finish()
