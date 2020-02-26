import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url",

    )
    parser.addoption("--status_code", action="store", default=200, help="This is status code")


@pytest.fixture
def paramses(request):
    return request.config.getoption("--url")



@pytest.fixture
def status(request):
    return int(request.config.getoption("--status_code"))