import allure
import pytest
from pages.group_page import Group
from pages.profile_page import Profile


@allure.story("Extended test")
@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест создания группы: имя - №-timestamp, тип - Признак договора, признак - Рандом')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_group_attr_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
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
    group.dropdown_without_input(group.group_type_select, "Признак Договора")
    # Ввод случайного признака
    group.input_in_field(group.params_input, group.random_value_float_str(100, 5000))
    # Клик по кнопке создания группы
    group.click_button(group.create_group_button, do_assert=True)
    # Клик по кнопке подтверждения добавления группы
    group.click_button(group.confirm_add_button)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест создания группы: имя - №-timestamp, тип - Заказчик, заказчик - Рандом')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_group_client_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
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
    group.dropdown_without_input(group.group_type_select, "Заказчик")
    # Ввод случайного заказчика
    group.input_in_field(group.params_input, group.random_value_float_str(100, 5000))
    # Клик по кнопке создания группы
    group.click_button(group.create_group_button, do_assert=True)
    # Клик по кнопке подтверждения добавления группы
    group.click_button(group.confirm_add_button)
    # Конец теста


@allure.story("Extended test")
@allure.feature('Создание групп')
@allure.description('ЛКЭ. Тест удалания группы: группа - Шестая в списке')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_group_delete_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture
    
    # Переход в профиль
    sidebar.click_button(sidebar.profile_button, do_assert=True)
    
    profile = Profile(base.driver)
    # Переход на вкладку групп
    profile.click_button(profile.groups_tab)
    # Клик по кнопке удаления группы
    profile.click_button(profile.groups_delete_button)
    # Клик по кнопке подтверждения удаления
    profile.click_button(profile.confirm_button, wait="lst")
    # Конец теста
