import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

# User = settings.AUTH_USER_MODEL

# class Applicant(models.Model):
# user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class MaritalStatus(models.Model):
    status = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "marital status"
        verbose_name_plural = "marital statuses"

    def __str__(self):
        return self.status.title()

    def get_absolute_url(self):
        return reverse("marital_status_detail", kwargs={"pk": self.pk})


class Religion(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "religion"
        verbose_name_plural = "religions"

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse("maritalStatus_detail", kwargs={"pk": self.pk})


class Nationality(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "nationality"
        verbose_name_plural = "nationalities"

    def __str__(self):
        return self.name.title()


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name.title()


class Applicant(models.Model):
    # applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    last_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    alias_name = models.TextField(blank=True)
    ht_ft = models.FloatField("height", help_text="add your height in feet", default=0)
    ht_in = models.FloatField(
        "height", help_text="add your height in inches", default=0
    )
    wt_ks = models.FloatField("height in kilos", default=0)
    wt_lbs = models.FloatField("height in pounds", default=0)
    marks = models.TextField("any distinguishing marks", blank=True)
    dob = models.DateField("date of birth", null=True)
    pob = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, verbose_name="place of birth"
    )
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True)
    overstayed = models.BooleanField(
        "have you overstayed in any country",
        default=False,
        help_text="<br>Please check box if, Yes",
    )
    convicted = models.BooleanField(
        "have you ever been convicted or charged in St Lucia or any other country?",
        default=False,
        help_text="Please check box if, Yes",
    )
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)
    marital_status = models.ForeignKey(
        MaritalStatus, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = "applicant"
        verbose_name_plural = "applicants"

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("applicants:applicant-detail", kwargs={"pk": self.pk})

    def get_full_name(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name[0]}"

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(str(self.uid) + "-" + self.title)
    #     super(Incoming, self).save(*args, **kwargs)


class Passport(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    passport_number = models.CharField(max_length=10, unique=True)
    date_issued = models.DateField()
    place_of_issue = models.CharField(max_length=50)

    class Meta:
        verbose_name = "passport"
        verbose_name_plural = "passports"

    def __str__(self):
        return self.passport_number

    def get_absolute_url(self):
        return reverse("passport_detail", kwargs={"pk": self.pk})


class Address(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    direction = models.TextField("directions to your home")

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"

    def __str__(self):
        return f"{self.address1}, {self.address2}"

    def get_absolute_url(self):
        return reverse("address_detail", kwargs={"pk": self.pk})


class Other(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    marital_status = models.ForeignKey(
        MaritalStatus, on_delete=models.SET_NULL, null=True
    )
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)
    children = models.IntegerField(default=0)
    dependents = models.IntegerField(default=0)

    class Meta:
        verbose_name = "other"
        verbose_name_plural = "others"

    def __str__(self):
        return f"{self.marital_status.status}, {self.religion.name}, {self.children}, {self.dependents}"

    def get_absolute_url(self):
        return reverse("other_detail", kwargs={"pk": self.pk})


class Contact(models.Model):
    tel1 = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={"pk": self.pk})
