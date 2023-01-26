import random
from dataclasses import dataclass

import calendar
from faker import Faker

@dataclass
class User:
        first_name: str = None
        last_name: str = None
        email: str = None
        email_mismatch: str = None
        password: str = None
        password_mismatch: str = None
        company: str = None
        day_of_birth: str = None
        month_of_birth: str = None
        year_of_birth: str = None
        gender: str = None

faker_en = Faker('En')

def generate_user():
    return User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        email_mismatch=faker_en.email(),
        password=faker_en.password(),
        password_mismatch=faker_en.password(),
        company=faker_en.company(),
        day_of_birth=faker_en.day_of_month(),
        month_of_birth=faker_en.month_name(),
        year_of_birth=faker_en.year(),
        gender=random.choice(('Male', 'Female'))
    )
# REGISTRATION_DATA

# REGISTRATION_FIRST_NAME = 'Andrew'
# REGISTRATION_LAST_NAME = 'Smith'
# REGISTRATION_PASSWORD = 'StrongPassword123'
# REGISTRATION_PASSWORD_MISMATCH = 'MismatchedStrongPassword123'
# REGISTRATION_COMPANY = 'DDD Records'
# REGISTRATION_DATE_OF_BIRTH = str(random.choice(list(range(1, 32))))
# REGISTRATION_MONTH_OF_BIRTH = random.choice(list(calendar.month_name)[1:])
# REGISTRATION_YEAR_OF_BIRTH = str(random.choice(list(range(1913, 2023))))
# REGISTRAION_GENDER = random.choice(('Male', 'Female'))


# LOGIN DATA
INVALID_EMAIL = 'invalid.email@gmail.com'
INVALID_PASSWORD = 'invalid123'
VALID_EMAIL = 'email@gmail.com'
VALID_PASSWORD = '123123'
