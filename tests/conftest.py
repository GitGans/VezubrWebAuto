import allure
import pytest
import requests
from pages.login import accounts
from tests.base_test import base_test_with_login, base_test_without_login, base_test_with_login_via_link


def pytest_addoption(parser):
    parser.addoption("--domain", choices=['dev', 'com', 'ru'], action="store", default="com",
                     help="Set the domain for tests")


# Фикстура для базового URL API на основе домена
@pytest.fixture
def api_base_url(domain):
    return f"https://api.vezubr.{domain}/v1/api"


@pytest.fixture
def api_login(api_base_url):
    def _login(role: str):
        if role not in accounts:
            raise KeyError(f"Role '{role}' not found in accounts")
        
        login_url = f"{api_base_url}/user/login"
        payload = {
            "username": accounts[role]["email"],
            "password": accounts[role]["password"]
        }
        
        # Отправляем запрос на логин
        response = requests.post(login_url, json=payload)
        assert response.status_code == 200, f"Login failed for role {role}"
        
        # Получаем токен
        token = response.json().get("token")
        
        # Выводим токен в консоль
        print(f"Token for role '{role}': {token}")
        
        # Добавляем токен в шаг Allure
        with allure.step(f"Login successful for role '{role}', token: {token}"):
            pass  # Шаг отображается в отчете, можно добавить дополнительные действия если нужно
        
        return token
    
    return _login


@pytest.fixture
def domain(request):
    return request.config.getoption("--domain")


@pytest.fixture
def base_fixture(request, domain):
    # Проверяем, используется ли отчет Allure
    allure_dir = request.config.getoption("--alluredir", default=None)
    
    # Получаем параметр из теста, который определяет тип теста и роль
    role = request.param
    
    # Логика для выбора базового теста
    if role == 'without_login':
        base, login = base_test_without_login(domain)
        base.allure_dir = allure_dir  # Устанавливаем директорию в base, если используется Allure
        yield base, login
    elif role == 'via_link':
        base, login = base_test_with_login_via_link(domain)
        base.allure_dir = allure_dir
        yield base, login
    else:
        base, sidebar = base_test_with_login(domain, role)
        base.allure_dir = allure_dir
        yield base, sidebar
    
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
