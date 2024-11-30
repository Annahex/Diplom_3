from faker import Faker

_fake = Faker()
_email = _fake.email()
_password = _fake.password()


def get_email():
    return _email


def get_password():
    return _password
