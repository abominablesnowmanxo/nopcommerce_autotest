import pytest
import time

from tests.pages.login_page import LoginPage
from tests.pages.registration_page import RegistrationPage
from tests.data.random_data import generate_user
from tests.data.urls import LOGIN_PAGE_URL, REGISTRATION_PAGE_URL


class TestLoginFunctionality:
    @pytest.fixture(scope='function', autouse=True)
    def setup_method(self, driver):
        user = generate_user()
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.register_new_user(user.first_name, user.last_name, user.email, user.password)
        yield user


    #TC_LF_001
    def test_user_can_login_with_valid_email_and_valid_password(self, driver, setup_method):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_can_login_with_valid_email_and_valid_password(setup_method)
        page.user_redirected_to_main_page_after_successful_login()
        page.log_out_link_is_present()

    #TC_LF_002
    def test_user_cannot_login_with_invalid_email_and_invalid_password(self, driver, setup_method):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cannot_login_with_invalid_email_and_invalid_password(setup_method)
        page.should_be_no_customer_account_found_message()
        page.log_out_link_is_not_present()

    #TC_LF_003
    def test_user_cannot_login_with_valid_email_and_invalid_password(self, driver, setup_method):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cannot_login_with_valid_email_and_invalid_password(setup_method)
        page.should_be_credential_provided_are_incorrect_message()
        page.log_out_link_is_not_present()

    #TC_LF_004
    def test_user_cannot_login_with_invalid_email_and_valid_password(self, driver, setup_method):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cannot_login_with_invalid_email_and_valid_password(setup_method)
        page.should_be_no_customer_account_found_message()
        page.log_out_link_is_not_present()

    #TC_LF_005
    def test_user_cannot_login_with_empty_email_and_password_fields(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cannot_login_with_empty_email_and_password_fields()
        page.should_be_email_error_message()
        page.log_out_link_is_not_present()


class TestLoginPage:

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
