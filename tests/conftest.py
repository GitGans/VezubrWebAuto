import pytest


def pytest_addoption(parser):
    parser.addoption("--domain", choices=['dev', 'com', 'ru'], action="store", default="com",
                     help="Set the domain for tests")


@pytest.fixture
def domain(request):
    return request.config.getoption("--domain")
