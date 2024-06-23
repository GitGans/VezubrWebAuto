import allure
from tests.base_test import base_test_with_login
from pages.group_page import Group
from pages.profile_page import Profile


@allure.story("Extended test")
@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест создания группы: имя - №-timestamp, тип - Признак договора, признак - Рандом')
def test_group_attr_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход в профиль
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    
    profile = Profile(base.driver)
    # Переход на вкладку групп
    profile.click_button(profile.groups_tab)
    # Клик по кнопке добавления группы
    profile.click_button(profile.add_user_button)
    
    group = Group(base.driver)
    # Ввод имени группы
    group.input_in_field(group.title_input, f"№-{base.get_timestamp()}")
    # Выбор типа группы "Признак Договора"
    group.dropdown_click_input_click(group.group_type_select, "Признак Договора")
    # Ввод случайного признака
    group.input_in_field(group.params_input, group.random_value_float_str(100, 5000))
    # Клик по кнопке создания группы
    group.click_button(group.create_group_button, do_assert=True)
    # Клик по кнопке подтверждения добавления группы
    group.click_button(group.confirm_add_button)
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Extended test")
@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест создания группы: имя - №-timestamp, тип - Заказчик, заказчик - Рандом')
def test_group_client_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход в профиль
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    
    profile = Profile(base.driver)
    # Переход на вкладку групп
    profile.click_button(profile.groups_tab)
    # Клик по кнопке добавления группы
    profile.click_button(profile.add_user_button)
    
    group = Group(base.driver)
    # Ввод имени группы
    group.input_in_field(group.title_input, f"№-{base.get_timestamp()}")
    # Выбор типа группы "Заказчик"
    group.dropdown_click_input_click(group.group_type_select, "Заказчик")
    # Ввод случайного заказчика
    group.input_in_field(group.params_input, group.random_value_float_str(100, 5000))
    # Клик по кнопке создания группы
    group.click_button(group.create_group_button, do_assert=True)
    # Клик по кнопке подтверждения добавления группы
    group.click_button(group.confirm_add_button)
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Extended test")
@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест удалания группы: группа - Шестая в списке')
def test_group_delete_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход в профиль
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    
    profile = Profile(base.driver)
    # Переход на вкладку групп
    profile.click_button(profile.groups_tab)
    # Клик по кнопке удаления группы
    profile.click_button(profile.groups_delete_button)
    # Клик по кнопке подтверждения удаления
    profile.click_button(profile.confirm_button, wait="lst")
    
    # Завершение теста
    sidebar.test_finish()
