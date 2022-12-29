from selenium.webdriver.common.by import By


class BasePageLocators:
    MY_ACCOUNT_LINK = (By.LINK_TEXT, 'My account')
    LOG_OUT_LINK = (By.LINK_TEXT, 'Log out')


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, 'Email')
    PASSWORD_FIELD = (By.ID, 'Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.login-button')
    UNSUCCSESSFUL_LOGIN_MESSAGE = (By.XPATH, "//div[contains(text(), 'Login was unsuccessful')]")
    NO_ACCOUNT_FOUND_MESSAGE = (By.XPATH, "//div//li[contains(text(), 'No customer account found')]")


# class RegistrationPageLocators:
#     FIRST_NAME_FIELD = (By.ID, 'FirstName')
#     LAST_NAME_FIELD = (By.ID, 'LastName')
#     EMAIL_FIELD = (By.ID, 'Email')
#     PASSWORD_FIELD = (By.ID, 'Password')
#     CONFIRM_PASSWORD_FIELD = (By.ID, 'ConfirmPassword')
#     SUBMIT_BUTTON = (By.ID, 'register-button')
#     SUCCESSFUL_REGISTRAION_MESSAGE = (By.CSS_SELECTOR, '.result')
#     CONTINUE_BUTTON = (By.CSS_SELECTOR, '.register-continue-button')
