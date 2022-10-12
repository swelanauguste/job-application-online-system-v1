from django.core.management.base import BaseCommand

from ...models import MaritalStatus, Religion


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
        
        with open(f"lists/marital_status_list.txt") as file:
            for row in file:
                status = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{status} added"))
                MaritalStatus.objects.get_or_create(
                    status=status,
                )
        self.stdout.write(self.style.SUCCESS("list of martial statuses added"))
