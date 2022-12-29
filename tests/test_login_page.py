import pytest

from .pages.login_page import LoginPage
from tests.urls import LOGIN_PAGE_URL


def test_user_can_login_with_valid_email_and_valid_password(driver):
    page = LoginPage(driver, LOGIN_PAGE_URL)
    page.open_page()
    page.user_can_login_with_valid_email_and_valid_password()
    page.user_redirected_to_main_page_after_successful_login()
    page.log_out_link_is_present()

def test_user_cant_login_with_invalid_email_and_invalid_password(driver):
    page = LoginPage(driver, LOGIN_PAGE_URL)
    page.open_page()
    page.user_cant_login_with_invalid_email_and_invalid_password()
    page.should_be_no_customer_account_found_message()
    page.log_out_link_is_not_present()

def test_user_cant_login_with_valid_email_and_invalid_password(driver):
    page = LoginPage(driver, LOGIN_PAGE_URL)
    page.open_page()
    page.user_cant_login_with_valid_email_and_invalid_password()
    page.should_be_credential_provided_are_incorrect_message()
    page.log_out_link_is_not_present()

def test_user_cant_login_with_invalid_email_and_valid_password(driver):
    page = LoginPage(driver, LOGIN_PAGE_URL)
    page.open_page()
    page.user_cant_login_with_invalid_email_and_valid_password()
    page.should_be_no_customer_account_found_message()
    page.log_out_link_is_not_present()

def test_user_cant_login_with_empty_email_and_password_fields(driver):
    page = LoginPage(driver, LOGIN_PAGE_URL)
    page.open_page()
    page.user_cant_login_with_empty_email_and_password_fields()
    page.should_be_email_error_message()
    page.log_out_link_is_not_present()
