import allure
from tests.base_test import base_test_with_login


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЭ. Тест сортировок списков заявок по вссем столбцам')
def test_sorting_requests_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку активных FTL заявок
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=13, num_clicks=3, wait="lst")
    
    # Переход к списку заявок на доставку груза
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ltl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=9, num_clicks=3, wait="lst")
    
    # Завершение теста
    sidebar.test_finish()
    
    
@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКП. Тест сортировок списков заявок по вссем столбцам')
def test_sorting_requests_lkp(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkp'
    base, sidebar = base_test_with_login(domain=domain, role='lkp')
    
    # Переход к списку активных FTL заявок
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=12, num_clicks=3, wait="lst")
    
    # Переход к списку заявок на доставку груза
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ltl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=9, num_clicks=3, wait="lst")
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Extended test")
@allure.feature('Сортировки')
@allure.description('ЛКЗ. Тест сортировок списков заявок по вссем столбцам')
def test_sorting_requests_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
    # Переход к списку активных FTL заявок
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ftl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=12, num_clicks=3, wait="lst")
    
    # Переход к списку заявок на доставку груза
    base.move_and_click(move_to=sidebar.requests_hover, click_to=sidebar.ltl_active_list_button,
                        do_assert=True, wait="lst")
    # Клик по кнопке сброса фильтров
    base.click_button(base.reset_button, wait="lst")
    # Последовательный клик по всем кнопкам сортировки всех столбцов
    base.click_multiple_buttons(base.sorting_button, num_buttons=9, num_clicks=3, wait="lst")
    
    # Завершение теста
    sidebar.test_finish()
