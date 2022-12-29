
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)

    def is_element_present(self, by, selector):
        try:
            self.driver.find_element(by, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return True

        return False

    def log_out_link_is_present(self):
        assert self.is_element_present(*BasePageLocators.LOG_OUT_LINK), "No 'Log out' link is present"

    def log_out_link_is_not_present(self):
        assert self.is_not_element_present(*BasePageLocators.LOG_OUT_LINK), "'Log out' link is present"
