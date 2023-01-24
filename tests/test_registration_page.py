import pytest
import time
from .pages.registration_page import RegistrationPage
from tests.urls import REGISTRATION_PAGE_URL


class TestRegistraionPage:

    #TC_RF_001
    def test_user_can_register_providing_only_required_fields(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_can_registrer_providing_required_fields_only()
        page.should_be_registration_successful_message()
        page.should_be_continue_link_button()

    #TC_RF_002
    def test_user_can_register_providing_all_the_fields(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_can_register_providing_all_the_fields()
        page.should_be_registration_successful_message()
        page.should_be_continue_link_button()

    #TC_RF_003
    def test_user_cannot_register_without_providing_first_name_field(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_cannot_register_without_providing_first_name_field()
        page.should_be_first_name_error_message()
        page.user_stays_on_registration_page()

    #TC_RF_004
    def test_user_cannot_register_without_providing_last_name_field(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_cannot_register_without_providing_last_name_field()
        page.should_be_last_name_error_message()
        page.user_stays_on_registration_page()

    #TC_RF_005
    def test_user_cannot_register_without_providing_email_name_field(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_cannot_register_without_providing_email_field()
        page.should_be_email_error_message()
        page.user_stays_on_registration_page()

    #TC_RF_006
    def test_user_cannot_register_without_providing_password_field(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_cannot_register_without_providing_password_field()
        page.should_be_password_error_message()
        page.user_stays_on_registration_page()

    #TC_RF_007
    def test_user_cannot_register_without_providing_confirm_password_field(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_cannot_register_without_providing_confirm_password_field()
        page.should_be_confirm_password_error_message()
        page.user_stays_on_registration_page()

    #TC_RF_008
    @pytest.mark.new
    def test_user_cannot_register_if_password_and_confirm_password_fields_do_not_match(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_cannot_register_if_password_and_confirm_password_fields_do_not_match()
        page.should_be_passwords_mismatch_error_message()
        page.user_stays_on_registration_page()
