import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def driver(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    yield driver
    driver.quit()
