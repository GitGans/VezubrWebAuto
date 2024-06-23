import time
import allure
from tests.base_test import base_test_with_login
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList


@allure.story("Smoke test")
@allure.feature('Создание и операции с водителями')
@allure.description('ЛКЭ. Тест создания водителя Экс: ФИО - ФИО-timestamp, паспорт/права - РФ, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, добавить/убрать - 2 и 1 ТС, '
                    'работа - останавливаем/востанавливаем/увольняем')
def test_own_driver_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button, wait="form")
    
    add_driver = DriverAdd(base.driver)
    # Добавление нового водителя и получение его фамилии
    surname = add_driver.add_base_driver()
    
    # Фильтрация по фамилии водителя и переход к его профилю
    driver_list.input_in_field(driver_list.surname_filter, value=surname, wait="lst")
    driver_list.click_button(driver_list.first_driver_link, wait="form")
    
    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl, wait="form")
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl, wait="form")
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Прикрепить второй ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(1)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button, wait="form")
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button, wait="form")
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    
    # Завершение теста
    sidebar.test_finish()


@allure.story("Smoke test")
@allure.feature('Создание и операции с водителями')
@allure.description('ЛКЭ. Тест создания водителя внутр КА: ка - Первыйй в списке, ФИО - ВФИО-timestamp, '
                    'паспорт/права - РФ, № паспорт/код/права/тлф. - Рандом, добавить/убрать - 2 и 1 ТС, '
                    'работа - останавливаем/востанавливаем/увольняем')
def test_inner_driver_add_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button, wait="form")
    
    add_driver = DriverAdd(base.driver)
    # Добавление нового водителя и получение его фамилии
    surname = add_driver.add_base_inner_driver()
    
    # Фильтрация по фамилии водителя и переход к его профилю
    driver_list.input_in_field(driver_list.surname_filter, value=surname, wait="lst")
    driver_list.click_button(driver_list.first_driver_link, wait="form")
    
    # Включить тогл готов работать как грузчик
    add_driver.click_button(add_driver.work_as_loader_toggl, wait="form")
    # Включить тогл никогда не делегировать
    add_driver.click_button(add_driver.never_delegate_toggl, wait="form")
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    # Прикрепить первый ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Прикрепить второй ТС в списке
    add_driver.click_button(add_driver.select_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    time.sleep(1)
    # Клик по кнопке прикрепить ТС
    add_driver.click_button(add_driver.attach_button, wait="form")
    # Открепить первый ТС в списке
    add_driver.click_button(add_driver.unselect_button)
    # Клик по кнопке подтвердить прикрепление ТС
    add_driver.click_button(add_driver.assign_selected_button, wait="form")
    # Открытие меню действий - приостановка работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.suspend_work_button, wait="form")
    # Открытие меню действий - возобновления работы водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.ready_to_work_button, wait="form")
    # Открытие меню действий - увольнение водителя
    add_driver.click_button(add_driver.action_menu_button)
    add_driver.click_button(add_driver.fire_button)
    # Клик по кнопке подтверждения увольнения водителя
    add_driver.click_button(add_driver.yes_button, do_assert=True)
    # Подтверждение успешного увольнения водителя
    add_driver.click_button(add_driver.ok_button)
    
    # Завершение теста
    sidebar.test_finish()
