import pytest
import time
from .pages.login_page import LoginPage
from tests.urls import LOGIN_PAGE_URL


class TestLoginPage:
    def test_user_can_login_with_valid_email_and_valid_password_001(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_can_login_with_valid_email_and_valid_password()
        page.user_redirected_to_main_page_after_successful_login()
        page.log_out_link_is_present()


    def test_user_cant_login_with_invalid_email_and_invalid_password_002(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_invalid_email_and_invalid_password()
        page.should_be_no_customer_account_found_message()
        page.log_out_link_is_not_present()


    def test_user_cant_login_with_valid_email_and_invalid_password_003(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_valid_email_and_invalid_password()
        page.should_be_credential_provided_are_incorrect_message()
        page.log_out_link_is_not_present()


    def test_user_cant_login_with_invalid_email_and_valid_password_004(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_invalid_email_and_valid_password()
        page.should_be_no_customer_account_found_message()
        page.log_out_link_is_not_present()


    def test_user_cant_login_with_empty_email_and_password_fields_005(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.user_cant_login_with_empty_email_and_password_fields()
        page.should_be_email_error_message()
        page.log_out_link_is_not_present()


    def test_forgot_password_link_is_present_and_lead_to_password_recovery_page_006(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.should_be_forgot_password_link()
        page.user_can_go_to_password_recovery_page()


    def test_user_can_go_to_register_page_clicking_regiter_button_007(self, driver):
        page = LoginPage(driver, LOGIN_PAGE_URL)
        page.open_page()
        page.should_be_register_button()
        page.user_can_go_to_register_page_clicking_register_button()
