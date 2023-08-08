import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


CHROME_DRIVER = ChromeDriverManager().install()
# FIREFOX_DRIVER = GeckoDriverManager().install()
EDGE_DRIVER = EdgeChromiumDriverManager().install()


def pytest_addoption(parser):
    """
    Pytest hook to add custom command-line options for browser selection and headless mode.

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
    match browser:
        case 'chrome':
            options = ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(
                service=ChromeService(CHROME_DRIVER),
                options=options
            )
        case 'firefox':
            options = FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(options=options)
        case 'edge':
            options = EdgeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Edge(
                service=EdgeService(EDGE_DRIVER),
                options=options
            )
        case _:
            raise pytest.UsageError('--browser should be chrome, firefox or edge')
    driver.maximize_window()
    yield driver
    driver.quit()
