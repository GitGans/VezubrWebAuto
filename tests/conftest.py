import pytest
import os
from tests.base_test import base_test_with_login, base_test_without_login, base_test_with_login_via_link


def pytest_addoption(parser):
    parser.addoption("--domain", choices=['dev', 'com', 'ru'], action="store", default="com",
                     help="Set the domain for tests")


@pytest.fixture
def domain(request):
    return request.config.getoption("--domain")


@pytest.fixture
def base_fixture(request, domain):
    # Ищем директорию, которая начинается с 'results_'
    allure_dir = None
    for dir_name in os.listdir('.'):
        if dir_name.startswith('results_') and os.path.isdir(dir_name):
            allure_dir = os.path.abspath(dir_name)  # Сохраняем путь к найденной директории
            print(f"Allure directory found and set: {allure_dir}")
            break
    
    # Получаем параметр из теста, который определяет тип теста и роль
    role = request.param
    
    # Логика для выбора базового теста
    if role == 'without_login':
        base, login = base_test_without_login(domain)
        base.allure_dir = allure_dir  # Устанавливаем директорию в base
        yield base, login  # Возвращаем base и login вместо sidebar
    elif role == 'via_link':
        base, login = base_test_with_login_via_link(domain)
        base.allure_dir = allure_dir  # Устанавливаем директорию в base
        yield base, login  # Возвращаем base и login вместо sidebar
    else:
        base, sidebar = base_test_with_login(domain, role)
        base.allure_dir = allure_dir  # Устанавливаем директорию в base
        yield base, sidebar  # Возвращаем base и sidebar
    
    # Завершаем сессию драйвера после выполнения теста
    base.test_finish()


# Хук для сохранения скриншота в случае провала теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Вызов теста и получение его результата
    outcome = yield
    report = outcome.get_result()
    
    # Получаем кортеж (base, sidebar) через фикстуру
    base_fixture = item.funcargs.get('base_fixture', None)
    
    if base_fixture:
        base, _ = base_fixture  # Извлекаем base из кортежа
        
        # Если тест завершился с ошибкой и base доступен
        if report.when == "call" and report.failed and base:
            # Получаем имя теста
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            base.get_screenshot(test_name)  # Передаем имя теста в метод скриншота
