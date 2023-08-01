from selenium.webdriver.common.by import By


class BasePageLocators:
    LOG_OUT_LINK = (By.CSS_SELECTOR, '.ico-logout')
    MY_ACCOUNT_LINK = (By.CSS_SELECTOR, '.ico-account')


class LoginPageLocators:
    CREDENTIALS_ARE_INCORRECT_MESSAGE = (
        By.CSS_SELECTOR, ".message-error ul li")
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    EMAIL_ERROR = (By.CSS_SELECTOR, '#Email-error')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '.forgot-password a')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.login-button')
    NO_ACCOUNT_FOUND_MESSAGE = (By.CSS_SELECTOR, ".message-error ul li")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register-button")


class RegistrationPageLocators:
    COMPANY_NAME = (By.CSS_SELECTOR, '#Company')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '.register-continue-button')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#ConfirmPassword')
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, '#ConfirmPassword-error')
    DAY_OF_BIRTH = (By.CSS_SELECTOR, "select[name='DateOfBirthDay']")
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    EMAIL_ERROR = (By.CSS_SELECTOR, '#Email-error')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#FirstName')
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, '#FirstName-error')
    GENDER_RADIO_MALE = (By.CSS_SELECTOR, '#gender-male')
    GENDER_RADIO_FEMALE = (By.CSS_SELECTOR, '#gender-female')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#LastName')
    LAST_NAME_ERROR = (By.CSS_SELECTOR, '#LastName-error')
    MONTH_OF_BIRTH = (By.CSS_SELECTOR, "select[name='DateOfBirthMonth']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    PASSWORD_ERROR = (By.CSS_SELECTOR, '#Password-error')
    SHORT_PASSWORD_ERROR = (By.CSS_SELECTOR, 'span#Password-error ul li')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#register-button')
    SUCCESSFUL_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '.result')
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, "select[name='DateOfBirthYear']")
