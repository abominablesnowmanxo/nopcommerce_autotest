import time
from .pages.login_page import LoginPage


url = 'https://demo.nopcommerce.com/login'


def test_user_can_register_with_required_fields(driver):
    page = LoginPage(driver, url)
    page.open_page()
    page.user_can_login_with_valid_email_and_valid_password()
    page.user_redirected_to_main_page_after_successful_login()
    page.log_out_link_is_present()
    page.my_account_link_is_present()
