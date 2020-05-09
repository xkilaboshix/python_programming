import pytest


@pytest.fixture
def csv_file():
    return 'csv_file!!!'

def pytest_addoption(parser):
    parser.addoption('--os-name', default='kinux', help='os name')
