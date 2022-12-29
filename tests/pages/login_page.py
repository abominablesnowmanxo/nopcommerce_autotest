from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators
from tests.test_data import INVALID_EMAIL, INVALID_PASSWORD, VALID_EMAIL, VALID_PASSWORD
from tests.urls import MAIN_PAGE_URL

class LoginPage(BasePage):
    def user_can_login_with_valid_email_and_valid_password(self):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(VALID_EMAIL)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(VALID_PASSWORD)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def user_redirected_to_main_page_after_successful_login(self):
        print(self.driver.current_url)
        assert self.driver.current_url == MAIN_PAGE_URL, "User was not redirected to Home Page"

    def test_user_cant_login_with_invalid_email_and_invalid_password(self):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(INVALID_EMAIL)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(INVALID_PASSWORD)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_no_customer_account_found_message(self):
        message = self.driver.find_element(*LoginPageLocators.NO_ACCOUNT_FOUND_MESSAGE)
        assert message.text == 'No customer account found'

    def user_cant_login_with_valid_email_and_invalid_password(self):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(VALID_EMAIL)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(INVALID_PASSWORD)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_credential_provided_are_incorrect_message(self):
        message = self.driver.find_element(*LoginPageLocators.CREDENTIALS_ARE_INCORRECT_MESSAGE)
        assert message.text == 'The credentials provided are incorrect'
