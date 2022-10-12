from django.contrib import admin

from .models import Passport, Address, MaritalStatus, Other, Contact, Applicant, Religion

admin.site.register(Passport)
admin.site.register(Address)
admin.site.register(MaritalStatus)
admin.site.register(Other)
admin.site.register(Contact)
admin.site.register(Applicant)
admin.site.register(Religion)