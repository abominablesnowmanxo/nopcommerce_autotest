import allure

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.locators import BasePageLocators


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        """
        Opens the page in the browser.
        """
        with allure.step(f'Open the page: {self.url}'):
            self.driver.get(self.url)

    def select_from_dropdown_menu(self, by, selector) -> Select:
        """
        Selects an option from a dropdown menu by its locator.

        Args:
            by (str): The type of the locator (e.g., 'id', 'name', 'css_selector').
            selector (str): The locator value.

        Returns:
            selenium.webdriver.support.select.Select: The Select object representing the dropdown menu.
        """
        try:
            return Select(self.driver.find_element(by, selector))
        except NoSuchElementException as error:
            raise error


    def element_is_present(self, by, selector: str) -> bool:
        """
        Checks if an element is present on the page.

        Args:
            by (str): The type of the locator (e.g., 'id', 'name', 'css_selector').
            selector (str): The locator value.

        Returns:
            bool: True if the element is present, False otherwise.
        """
        try:
            self.driver.find_element(by, selector)
        except NoSuchElementException:
            return False
        return True

    def element_is_not_present(self, by: str, selector: str, timeout=4) -> bool:
        """
        Checks if an element is not present on the page within the given timeout.

        Args:
            by (str): The type of the locator (e.g., 'id', 'name', 'css_selector').
            selector (str): The locator value.
            timeout (int, optional): The maximum time to wait for the element to be absent (default is 4 seconds).

        Returns:
            bool: True if the element is not present within the timeout, False otherwise.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_all_elements_located((by, selector)))
        except TimeoutException:
            return True

        return False

    def log_out_link_is_present(self):
        """
        Asserts that the "Log out" link is present on the page.

        Raises:
            AssertionError: If the "Log out" link is not present.
        """
        with allure.step('Check that Logout link is present on the page'):
            assert self.element_is_present(*BasePageLocators.LOG_OUT_LINK), \
                   "'Log out' link is not present"

    def log_out_link_is_not_present(self):
        """
        Asserts that the "Log out" link is not present on the page.

        Raises:
            AssertionError: If the "Log out" link is present.
        """
        with allure.step('Check that Logout link is not present on the page'):
            assert self.element_is_not_present(*BasePageLocators.LOG_OUT_LINK), \
                   "'Log out' link is present"
