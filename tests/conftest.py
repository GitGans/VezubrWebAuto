import pytest
from base.base_class import Base
from tests.base_test import base_test_with_login


def pytest_addoption(parser):
    parser.addoption("--domain", choices=['dev', 'com', 'ru'], action="store", default="com",
                     help="Set the domain for tests")


@pytest.fixture
def domain(request):
    return request.config.getoption("--domain")


@pytest.fixture
def base_fixture(request, domain):
    # Получаем роль из самого теста через параметризацию
    role = request.param
    
    # Инициализируем базовый тест с логином через Base
    base, sidebar = base_test_with_login(domain, role)
    
    # Возвращаем объект base для дальнейшего использования в тесте
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
            base.get_screenshot()
