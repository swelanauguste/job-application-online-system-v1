from django.core.management.base import BaseCommand

from ...models import Country, District, MaritalStatus, Nationality, Religion


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"lists/religion_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                Religion.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of religions added"))

        # ========================================================================================

        with open(f"lists/marital_status_list.txt") as file:
            for row in file:
                status = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{status} added"))
                MaritalStatus.objects.get_or_create(
                    status=status,
                )
        self.stdout.write(self.style.SUCCESS("list of martial statuses added"))

        # ========================================================================================

        with open(f"lists/country_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                Country.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of countries added"))

        # ========================================================================================

        with open(f"lists/nationality_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                Nationality.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of nationalities added"))
        # ========================================================================================

        with open(f"lists/district_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                District.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of districts added"))
