from faker import Faker


def email():
    return Faker("ru_RU").email()


def password():
    return Faker("ru_RU").password()
