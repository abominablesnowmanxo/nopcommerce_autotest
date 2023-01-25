import random
import calendar


# REGISTRATION_DATA
REGISTRATION_FIRST_NAME = 'Andrew'
REGISTRATION_LAST_NAME = 'Smith'
REGISTRATION_PASSWORD = 'StrongPassword123'
REGISTRATION_PASSWORD_MISMATCH = 'MismatchedStrongPassword123'
REGISTRATION_COMPANY = 'DDD Records'
REGISTRATION_DATE_OF_BIRTH = str(random.choice(list(range(1, 32))))
REGISTRATION_MONTH_OF_BIRTH = random.choice(list(calendar.month_name)[1:])
REGISTRATION_YEAR_OF_BIRTH = str(random.choice(list(range(1913, 2023))))
REGISTRAION_GENDER = random.choice(('Male', 'Female'))


# LOGIN DATA
INVALID_EMAIL = 'invalid.email@gmail.com'
INVALID_PASSWORD = 'invalid123'
VALID_EMAIL = 'email@gmail.com'
VALID_PASSWORD = '123123'
