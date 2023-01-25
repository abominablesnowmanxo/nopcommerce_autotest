import pytest
import time

from tests.test_data import (
    REGISTRATION_FIRST_NAME, REGISTRATION_LAST_NAME, VALID_EMAIL,
    VALID_PASSWORD)
from .pages.login_page import LoginPage
from .pages.registration_page import RegistrationPage
from tests.urls import LOGIN_PAGE_URL, REGISTRATION_PAGE_URL


class TestLoginPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup_method(self, driver):
        firstname = REGISTRATION_FIRST_NAME
        lastname = REGISTRATION_LAST_NAME
        email = VALID_EMAIL
        password = VALID_PASSWORD
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.register_new_user(firstname, lastname, email, password)


    #TC_LF_001
    def test_user_can_login_with_valid_email_and_valid_password(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_can_login_with_valid_email_and_valid_password()
        page.user_redirected_to_main_page_after_successful_login()
        page.log_out_link_is_present()

    #TC_LF_002
    def test_user_cant_login_with_invalid_email_and_invalid_password(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_invalid_email_and_invalid_password()
        page.should_be_no_customer_account_found_message()
        page.log_out_link_is_not_present()

    #TC_LF_003
    def test_user_cant_login_with_valid_email_and_invalid_password(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_valid_email_and_invalid_password()
        page.should_be_credential_provided_are_incorrect_message()
        page.log_out_link_is_not_present()

    #TC_LF_004
    def test_user_cant_login_with_invalid_email_and_valid_password(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_invalid_email_and_valid_password()
        page.should_be_no_customer_account_found_message()
        page.log_out_link_is_not_present()

    #TC_LF_005
    def test_user_cant_login_with_empty_email_and_password_fields(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_empty_email_and_password_fields()
        page.should_be_email_error_message()
        page.log_out_link_is_not_present()

    #TC_LF_006
    def test_forgot_password_link_is_present_and_lead_to_password_recovery_page(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.should_be_forgot_password_link()
        page.user_can_go_to_password_recovery_page()

    #TC_LF_007
    def test_user_can_go_to_register_page_clicking_regiter_button(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.should_be_register_button()
        page.user_can_go_to_register_page_clicking_register_button()
