import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def driver(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
