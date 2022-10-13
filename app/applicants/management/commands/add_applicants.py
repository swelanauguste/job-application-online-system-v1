import datetime
from random import randint, uniform

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Applicant, Country, Nationality, MaritalStatus, Religion


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            Applicant.objects.get_or_create(
                first_name=fake.first_name_nonbinary(),
                last_name=fake.last_name(),
                middle_name=fake.last_name(),
                ht_ft = round(uniform(5.5, 6.8), 1),
                wt_lbs = randint(90, 172),
                dob=fake.date_between_dates(datetime.date(1988, 1,1), datetime.date(2004, 12, 31)),
                pob=Country.objects.get(pk=randint(140, 190)),
                nationality=Nationality.objects.get(pk=randint(140, 190)),
                overstayed=randint(0, 1),
                convicted=randint(0, 1),
                religion=Religion.objects.get(pk =randint(1, 7)),
                marital_status=MaritalStatus.objects.get(pk =randint(1, 6))
            )
