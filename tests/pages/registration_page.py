from .base_page import BasePage
from .locators import RegistrationPageLocators
from tests.random_data import random_email
from tests.test_data import REGISTRAION_FIRST_NAME, REGISTRAION_LAST_NAME, REGISTRAION_PASSWORD


class RegistrationPage(BasePage):
    def user_registration_with_required_fields_only(self):
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(REGISTRAION_FIRST_NAME)
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME_FIELD).send_keys(REGISTRAION_LAST_NAME)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(random_email())
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRAION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(REGISTRAION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def should_be_registration_successful_message(self):
        message = self.driver.find_element(*RegistrationPageLocators.SUCCESSFUL_REGISTRAION_MESSAGE)
        assert message.text == 'Your registration completed', 'Registration was unsuccessful'

    def should_be_continue_link_button(self):
        assert self.is_element_present(*RegistrationPageLocators.CONTINUE_BUTTON), "'Continue' button is not present"
