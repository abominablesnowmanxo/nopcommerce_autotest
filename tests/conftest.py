import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser: chrome, firefox, edge')
    parser.addoption('--headless', action='store_true', default=False)


@pytest.fixture(scope='function')
def driver(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        options = ChromeOptions()
        if request.config.getoption('headless'):
            options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        if request.config.getoption('headless'):
            options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser == 'edge':
        options = EdgeOptions()
        if request.config.getoption('headless'):
            options.headless = True
        driver = webdriver.Edge(options=options)
    else:
        raise pytest.UsageError('--browser should be chrome, firefox or edge')
    driver.maximize_window()
    yield driver
    driver.quit()
