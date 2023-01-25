import string
import random


def random_email():
    letters = [random.choice(string.ascii_lowercase) for _ in range(0, 7)]
    rand_email = ''.join(letters) + '@gmail.com'
    return rand_email
