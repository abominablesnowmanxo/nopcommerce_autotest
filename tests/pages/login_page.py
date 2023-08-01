import allure

from tests.pages.base_page import BasePage
from tests.pages.locators import LoginPageLocators
from tests.data.user_model import User
from tests.data.urls import (
    MAIN_PAGE_URL, PASSWORD_RECOVERY_URL, REGISTRATION_PAGE_URL)


class LoginPage(BasePage):

    @allure.step('Enter email: {email}')
    def enter_email(self, email):
        self.driver.find_element(
            *LoginPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step('Enter password: {password}')
    def enter_password(self, password):
        self.driver.find_element(
            *LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Click \'Login\' button')
    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Click \'Register\' button')
    def click_register_button(self):
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    @allure.step('Click \'Forgot password\' link')
    def click_forgot_password_link(self):
        self.driver.find_element(*LoginPageLocators.FORGOT_PASSWORD).click()

    def user_can_login_with_valid_email_and_valid_password(self, user: User):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_login_button()

    @allure.step('Check that user redirected to the main page')
    def user_redirected_to_main_page_after_successful_login(self):
        assert self.driver.current_url == MAIN_PAGE_URL, \
               "User was not redirected to Home Page"

    def user_cannot_login_with_invalid_email_and_invalid_password(
            self,
            user: User
            ):
        self.enter_email(user.email_mismatch)
        self.enter_password(user.password_mismatch)
        self.click_login_button()

    @allure.step('Check that \'No customer account found\' error is present')
    def should_be_no_customer_account_found_message(self):
        message = self.driver.find_element(
            *LoginPageLocators.NO_ACCOUNT_FOUND_MESSAGE)
        assert message.text == 'No customer account found', \
               "'No customer account found' is not present"

    def user_cannot_login_with_valid_email_and_invalid_password(
            self,
            user: User
            ):
        self.enter_email(user.email)
        self.enter_password(user.password_mismatch)
        self.click_login_button()

    @allure.step('Check that \'Incorrect credintials\' error is present')
    def should_be_credential_provided_are_incorrect_message(self):
        message = self.driver.find_element(
            *LoginPageLocators.CREDENTIALS_ARE_INCORRECT_MESSAGE)
        assert message.text == 'The credentials provided are incorrect'

    def user_cannot_login_with_invalid_email_and_valid_password(
            self,
            user: User
            ):
        self.enter_email(user.email_mismatch)
        self.enter_password(user.password)
        self.click_login_button()

    def user_cannot_login_with_empty_email_and_password_fields(self):
        self.click_login_button()

    @allure.step('Check that \'Email\' error is present')
    def should_be_email_error_message(self):
        message = self.driver.find_element(*LoginPageLocators.EMAIL_ERROR)
        assert message.text == 'Please enter your email'

    @allure.step('Check that user is redirected to password recovery page')
    def user_can_go_to_password_recovery_page(self):
        self.click_forgot_password_link()
        assert self.driver.current_url == PASSWORD_RECOVERY_URL, \
               "User was not redirected to password recovery page"

    @allure.step('Check that \'Forgot password\' link is present')
    def should_be_forgot_password_link(self):
        assert self.element_is_present(*LoginPageLocators.FORGOT_PASSWORD), \
               "'Forgot Password?' link is not present"

    @allure.step('Check that user is redirected to registration page')
    def user_can_go_to_register_page_clicking_register_button(self):
        self.click_register_button()
        assert self.driver.current_url == REGISTRATION_PAGE_URL, \
               "User was not redirected to registration page"

    @allure.step('Check that \'Register\' button is present')
    def should_be_register_button(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_BUTTON), \
               "'Register' button is not present"
