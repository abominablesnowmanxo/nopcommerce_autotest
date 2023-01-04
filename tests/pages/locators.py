from selenium.webdriver.common.by import By


class BasePageLocators:
    MY_ACCOUNT_LINK = (By.CSS_SELECTOR, '.ico-account')
    LOG_OUT_LINK = (By.CSS_SELECTOR, '.ico-logout')


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, 'Email')
    PASSWORD_FIELD = (By.ID, 'Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.login-button')
    NO_ACCOUNT_FOUND_MESSAGE = (By.CSS_SELECTOR, ".message-error ul li")
    CREDENTIALS_ARE_INCORRECT_MESSAGE = (By.CSS_SELECTOR, ".message-error ul li")
    EMAIL_ERROR = (By.CSS_SELECTOR, '#Email-error')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '.forgot-password a')
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register-button")


# class RegistrationPageLocators:
#     FIRST_NAME_FIELD = (By.ID, 'FirstName')
#     LAST_NAME_FIELD = (By.ID, 'LastName')
#     EMAIL_FIELD = (By.ID, 'Email')
#     PASSWORD_FIELD = (By.ID, 'Password')
#     CONFIRM_PASSWORD_FIELD = (By.ID, 'ConfirmPassword')
#     SUBMIT_BUTTON = (By.ID, 'register-button')
#     SUCCESSFUL_REGISTRAION_MESSAGE = (By.CSS_SELECTOR, '.result')
#     CONTINUE_BUTTON = (By.CSS_SELECTOR, '.register-continue-button')
