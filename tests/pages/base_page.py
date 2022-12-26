from selenium.common.exceptions import NoSuchElementException


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
