import pytest


@pytest.fixture()
def browser():
    print('Выполняюсь перед тестом')

    yield

    print('Завершаю браузер')


@pytest.fixture()
def main_page(browser):
    pass




def test_first(browser, user,main_page):
    print('Тело теста')


def test_second(browser, user,main_page):
    print('Тело теста')
