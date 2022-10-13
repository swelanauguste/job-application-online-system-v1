import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Address, Applicant, District


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            Address.objects.get_or_create(
                applicant=Applicant.objects.get(pk=random.randint(1, 10)),
                address1=fake.address(),
                address3=District.objects.get(pk=random.randint(1, 18)),
                direction=fake.paragraph(nb_sentences=3),
            )
