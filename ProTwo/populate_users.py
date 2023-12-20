import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
django.setup()

from appTwo.models import User
from faker import Faker

fake = Faker()


def populate_users(n=5):
    for entry in range(n):
        fake_name = fake.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake.email()

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating fake data")
    populate_users(20)
    print("Done")
