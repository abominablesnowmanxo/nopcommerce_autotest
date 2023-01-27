import random
from faker import Faker

from tests.data.user_model import User

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
        day_of_birth=str(random.choice(list(range(1, 32)))),
        month_of_birth=faker_en.month_name(),
        year_of_birth=str(random.choice(list(range(1913, 2023)))),
        gender=random.choice(('Male', 'Female'))
    )
