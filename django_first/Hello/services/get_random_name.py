from faker import Faker

faker = Faker()


def get_random_name() -> str:
    return faker.first_name()
