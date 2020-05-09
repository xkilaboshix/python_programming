import pytest


@pytest.fixture
def csv_file():
    with open('test.csv', 'w') as c:
        print('before test')
        yield c
        print('after test')

def pytest_addoption(parser):
    parser.addoption('--os-name', default='kinux', help='os name')
