import time
from .base_page import BasePage
from .locators import RegistrationPageLocators
from tests.random_data import random_email
from tests.test_data import (
    REGISTRATION_FIRST_NAME, REGISTRATION_LAST_NAME, REGISTRATION_PASSWORD,
    REGISTRATION_COMPANY, REGISTRATION_DATE_OF_BIRTH, REGISTRATION_MONTH_OF_BIRTH,
    REGISTRATION_YEAR_OF_BIRTH)
from tests.urls import REGISTRATION_PAGE_URL


class RegistrationPage(BasePage):
    def user_can_registrer_providing_required_fields_only(self):
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(REGISTRATION_FIRST_NAME)
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME_FIELD).send_keys(REGISTRATION_LAST_NAME)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(random_email())
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def user_can_register_providing_all_the_fields(self):
        self.driver.find_element(*RegistrationPageLocators.GENDER_RADIO_MALE).click()
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(REGISTRATION_FIRST_NAME)
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME_FIELD).send_keys(REGISTRATION_LAST_NAME)
        self.select_from_dropdown_menu(*RegistrationPageLocators.DAY_OF_BIRTH).select_by_value(REGISTRATION_DATE_OF_BIRTH)
        self.select_from_dropdown_menu(*RegistrationPageLocators.MONTH_OF_BIRTH).select_by_visible_text(REGISTRATION_MONTH_OF_BIRTH)
        self.select_from_dropdown_menu(*RegistrationPageLocators.YEAR_OF_BIRTH).select_by_value(REGISTRATION_YEAR_OF_BIRTH)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(random_email())
        self.driver.find_element(*RegistrationPageLocators.COMPANY_NAME).send_keys(REGISTRATION_COMPANY)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()


    def should_be_registration_successful_message(self):
        message = self.driver.find_element(*RegistrationPageLocators.SUCCESSFUL_REGISTRAION_MESSAGE)
        assert message.text == 'Your registration completed', 'Registration was unsuccessful'

    def should_be_continue_link_button(self):
        assert self.is_element_present(*RegistrationPageLocators.CONTINUE_BUTTON), "'Continue' button is not present"

    def user_cant_register_without_providing_first_name_field(self):
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME_FIELD).send_keys(REGISTRATION_LAST_NAME)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(random_email())
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def user_cant_register_without_providing_last_name_field(self):
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(REGISTRATION_FIRST_NAME)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(random_email())
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def user_cant_register_without_providing_email_field(self):
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(REGISTRATION_FIRST_NAME)
        self.driver.find_element(*RegistrationPageLocators.LAST_NAME_FIELD).send_keys(REGISTRATION_LAST_NAME)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(REGISTRATION_PASSWORD)
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def should_be_first_name_error_message(self):
        message = self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_ERROR)
        assert message.text == 'First name is required.', "'First name is required.' message is not present"

    def should_be_last_name_error_message(self):
        message = self.driver.find_element(*RegistrationPageLocators.LAST_NAME_ERROR)
        assert message.text == 'Last name is required.', "'Last name is required.' message is not present"

    def should_be_email_error_message(self):
        message = self.driver.find_element(*RegistrationPageLocators.EMAIL_ERROR)
        assert message.text == 'Email is required.', "'Email is required.' message is not present"

    def user_stays_on_registration_page(self):
        assert self.driver.current_url == REGISTRATION_PAGE_URL
