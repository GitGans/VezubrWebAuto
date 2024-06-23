import allure
from tests.base_test import base_test_with_login
from pages.loader_add_page import LoaderAdd
from pages.loader_list_page import LoaderList


@allure.story("Smoke test")
@allure.feature('Создание и операции с специалистами')
@allure.description('ЛКЭ. Тест создания специалиста Экс: ФИО - ФИО-timestamp, паспорт - РФ, тип - Грузчик, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, работа - останавливаем/востанавливаем.')
def test_loader_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку специалистов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    
    loader_list = LoaderList(base.driver)
    # Клик по кнопке добавления специалиста
    loader_list.click_button(loader_list.add_loader_button, wait="form")
    
    add_loader = LoaderAdd(base.driver)
    # Добавление нового специалиста и получение его фамилии
    surname = add_loader.add_base_loader()
    
    # Фильтрация по фамилии специалиста и переход к его профилю
    loader_list.input_in_field(loader_list.surname_filter, value=surname, wait="lst")
    loader_list.click_button(loader_list.first_loader_link, wait="form")
    
    # Открытие меню действий - приостановка работы специалиста
    add_loader.click_button(add_loader.action_menu_button)
    add_loader.click_button(add_loader.suspend_work_button, wait="form")
    # Открытие меню действий - возобновление работы специалиста
    add_loader.click_button(add_loader.action_menu_button)
    add_loader.click_button(add_loader.ready_to_work_button, wait="form")
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание и операции с специалистами')
@allure.description('ЛКП. Тест создания специалиста Экс: ФИО - ФИО-timestamp, паспорт - РФ, тип - Грузчик, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, работа - останавливаем/востанавливаем.')
def test_loader_add_lkp(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkp'
    base, sidebar = base_test_with_login(domain=domain, role='lkp')
    
    # Переход к списку специалистов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.loaders_list_button,
                           do_assert=True, wait="lst")
    
    loader_list = LoaderList(base.driver)
    # Клик по кнопке добавления специалиста
    loader_list.click_button(loader_list.add_loader_button, wait="form")
    
    add_loader = LoaderAdd(base.driver)
    # Добавление нового специалиста и получение его фамилии
    surname = add_loader.add_base_loader()
    
    # Фильтрация по фамилии специалиста и переход к его профилю
    loader_list.input_in_field(loader_list.surname_filter, value=surname, wait="lst")
    loader_list.click_button(loader_list.first_loader_link, wait="form")
    
    # Открытие меню действий - приостановка работы специалиста
    add_loader.click_button(add_loader.action_menu_button)
    add_loader.click_button(add_loader.suspend_work_button, wait="form")
    # Открытие меню действий - возобновление работы специалиста
    add_loader.click_button(add_loader.action_menu_button)
    add_loader.click_button(add_loader.ready_to_work_button, wait="form")
    
    # Завершение теста
    sidebar.test_finish()
