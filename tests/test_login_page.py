import pytest

from .pages.login_page import LoginPage
from tests.urls import LOGIN_PAGE_URL


def test_user_can_login_with_valid_email_and_valid_password(driver):
    page = LoginPage(driver, LOGIN_PAGE_URL)
    page.open_page()
    page.user_can_login_with_valid_email_and_valid_password()
    page.user_redirected_to_main_page_after_successful_login()
    page.log_out_link_is_present()

@pytest.mark.new
def test_user_cant_login_with_invalid_email_and_invalid_password(driver):
    page = LoginPage(driver, LOGIN_PAGE_URL)
    page.open_page()
    page.test_user_cant_login_with_invalid_email_and_invalid_password()
    page.should_be_warning_message()
    page.log_out_link_is_not_present()
