from dataclasses import dataclass, field
from faker import Faker
import random

Faker.seed()

fake = Faker()

@dataclass
class User:
    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    email: str = field(default_factory=fake.email)
    email_mismatch: str = field(default_factory=fake.email)
    password: str = field(default_factory=fake.password)
    password_mismatch: str = field(default_factory=fake.password)
    company: str = field(default_factory=fake.company)
    day_of_birth: str = field(init=False)
    month_of_birth: str = field(init=False)
    year_of_birth: str = field(init=False)
    gender: str = field(default_factory=lambda: random.choice(('Male', 'Female')))

    def __post_init__(self):
        date_of_birth = fake.date_of_birth()
        self.day_of_birth = str(date_of_birth.day)
        self.month_of_birth = date_of_birth.strftime('%B')
        self.year_of_birth = str(date_of_birth.year)
