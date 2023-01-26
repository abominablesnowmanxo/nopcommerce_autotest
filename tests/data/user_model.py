from dataclasses import dataclass

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
