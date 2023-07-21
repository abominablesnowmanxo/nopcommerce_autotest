import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    """
    Pytest hook to add custom command-line options for browser selection and headless mode.

    Args:
        parser (pytest.Parser): The pytest command-line option parser.

    Usage:
        --browser: Choose the browser for test execution (chrome, firefox, edge).
        --headless: Run tests in headless mode (optional).
    """
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Choose browser: chrome, firefox, edge',
        choices=('chrome', 'firefox', 'edge')
    )
    parser.addoption(
        '--headless',
        action='store_true',
        default=False
    )


@pytest.fixture(scope='function')
def driver(request):
    """
    Pytest fixture to set up the WebDriver instance based on the specified browser option.

    Args:
        request (pytest.FixtureRequest): The pytest fixture request object.

    Returns:
        selenium.webdriver.remote.webdriver.WebDriver: WebDriver instance for the chosen browser.

    Usage:
        Use 'driver' as an argument in test functions to access the WebDriver instance.
    """
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    if browser == 'chrome':
        options = ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser == 'edge':
        options = EdgeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Edge(options=options)
    else:
        raise pytest.UsageError('--browser should be chrome, firefox or edge')
    driver.maximize_window()
    yield driver
    driver.quit()
