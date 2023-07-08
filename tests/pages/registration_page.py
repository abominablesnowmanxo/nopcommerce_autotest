from tests.pages.base_page import BasePage
from tests.pages.locators import RegistrationPageLocators
from tests.data.user_model import User
from tests.data.urls import REGISTRATION_PAGE_URL


class RegistrationPage(BasePage):

    def enter_first_name(self, firstname):
        self.driver.find_element(
            *RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(
            *RegistrationPageLocators.LAST_NAME_FIELD).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(
            *RegistrationPageLocators.EMAIL_FIELD).send_keys(email)

    def enter_company_name(self, company_name):
        self.driver.find_element(
            *RegistrationPageLocators.COMPANY_NAME).send_keys(company_name)

    def enter_password(self, password):
        self.driver.find_element(
            *RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(
            *RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)

    def enter_date_of_birth(self, day, month, year):
        self.select_from_dropdown_menu(
            *RegistrationPageLocators.DAY_OF_BIRTH).select_by_value(day)
        self.select_from_dropdown_menu(
            *RegistrationPageLocators.MONTH_OF_BIRTH).select_by_visible_text(month)
        self.select_from_dropdown_menu(
            *RegistrationPageLocators.YEAR_OF_BIRTH).select_by_value(year)

    def select_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(
                *RegistrationPageLocators.GENDER_RADIO_MALE).click()
        elif gender == 'Female':
            self.driver.find_element(
                *RegistrationPageLocators.GENDER_RADIO_FEMALE).click()

    def click_submit_button(self):
        self.driver.find_element(
            *RegistrationPageLocators.SUBMIT_BUTTON).click()

    def user_can_registrer_providing_required_fields_only(self):
        user = User()
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.enter_confirm_password(user.password)
        self.click_submit_button()

    def user_can_register_providing_all_the_fields(self):
        user = User()
        self.select_gender(user.gender)
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_date_of_birth(
            user.day_of_birth, user.month_of_birth, user.year_of_birth)
        self.enter_email(user.email)
        self.enter_company_name(user.company)
        self.enter_password(user.password)
        self.enter_confirm_password(user.password)
        self.click_submit_button()

    def should_be_registration_successful_message(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.SUCCESSFUL_REGISTRATION_MESSAGE)
        assert message.text == 'Your registration completed', \
               'Registration was unsuccessful'

    def should_be_continue_link_button(self):
        assert self.is_element_present(
            *RegistrationPageLocators.CONTINUE_BUTTON), \
                "'Continue' button is not present"

    def user_cannot_register_without_providing_first_name_field(self):
        user = User()
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.enter_confirm_password(user.password)
        self.click_submit_button()

    def should_be_first_name_error_message(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.FIRST_NAME_ERROR)
        assert message.text == 'First name is required.', \
               "'First name is required.' message is not present"

    def user_cannot_register_without_providing_last_name_field(self):
        user = User()
        self.enter_first_name(user.first_name)
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.enter_confirm_password(user.password)
        self.click_submit_button()

    def should_be_last_name_error_message(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.LAST_NAME_ERROR)
        assert message.text == 'Last name is required.', \
               "'Last name is required.' message is not present"

    def user_cannot_register_without_providing_email_field(self):
        user = User()
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_password(user.password)
        self.enter_confirm_password(user.password)
        self.click_submit_button()

    def should_be_email_error_message(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.EMAIL_ERROR)
        assert message.text == 'Email is required.', \
               "'Email is required.' message is not present"

    def user_cannot_register_without_providing_password_field(self):
        user = User()
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.click_submit_button()

    def should_be_password_error_message(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.PASSWORD_ERROR)
        assert message.text == 'Password is required.', \
               "'Password is required.' message is not present"

    def user_cannot_register_without_providing_confirm_password_field(self):
        user = User()
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_submit_button()

    def should_be_confirm_password_error_message(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.CONFIRM_PASSWORD_ERROR)
        assert message.text == 'Password is required.', \
               "'Password is required.' message is not present"

    def user_cannot_register_if_password_and_confirm_password_fields_do_not_match(self):
        user = User()
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.enter_confirm_password(user.password_mismatch)
        self.click_submit_button()

    def should_be_passwords_mismatch_error_message(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.CONFIRM_PASSWORD_ERROR)
        assert message.text == 'The password and confirmation password do not match.', \
            "'The password and confirmation password do not match.' message is not present"

    def user_stays_on_registration_page(self):
        assert self.driver.current_url == REGISTRATION_PAGE_URL

    def user_cannot_register_if_password_has_less_that_six_chars(self, short_password):
        user = User()
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.enter_password(short_password)
        self.enter_confirm_password(short_password)
        self.click_submit_button()

    def should_be_short_password_error_massage(self):
        message = self.driver.find_element(
            *RegistrationPageLocators.SHORT_PASSWORD_ERROR)
        assert message.text == 'must have at least 6 characters', \
               "'must have at least 6 characters' warning is not present"

    def register_new_user(self, firstname, lastname, email, password):
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_submit_button()
