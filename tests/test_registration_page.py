from .pages.registration_page import RegistrationPage
from tests.urls import REGISTRATION_PAGE_URL


class TestRegistraionPage:
    def test_user_can_register_with_only_required_fields(self, driver):
        page = RegistrationPage(driver, REGISTRATION_PAGE_URL)
        page.open_page()
        page.user_registration_with_required_fields_only()
        page.should_be_registration_successful_message()
        page.should_be_continue_link_button()
