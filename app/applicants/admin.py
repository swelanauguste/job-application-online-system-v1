from django.contrib import admin

from .models import (
    Address,
    Applicant,
    Contact,
    Country,
    MaritalStatus,
    Nationality,
    Other,
    Passport,
    Religion,
    District
)

admin.site.register(Passport)
admin.site.register(Address)
admin.site.register(MaritalStatus)
admin.site.register(Other)
admin.site.register(Contact)
admin.site.register(Applicant)
admin.site.register(Religion)
admin.site.register(Nationality)
admin.site.register(Country)
admin.site.register(District)
