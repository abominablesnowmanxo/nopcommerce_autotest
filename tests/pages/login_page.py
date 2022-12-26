from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def user_can_login_with_valid_email_and_valid_password(self):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys('countjeffrey@gmail.com')
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('123123')
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def user_redirected_to_main_page_after_successful_login(self):
        print(self.driver.current_url)
        assert self.driver.current_url == 'https://demo.nopcommerce.com/'

    def my_account_link_is_present(self):
        assert self.is_element_present(*MainPageLocators.MY_ACCOUNT_LINK)

    def log_out_link_is_present(self):
        assert self.is_element_present(*MainPageLocators.LOG_OUT_LINK)
