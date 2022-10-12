# Generated by Django 4.1.2 on 2022-10-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applicants", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant",
            name="ht_ft",
            field=models.FloatField(
                default=0, help_text="add your height in feet", verbose_name="height"
            ),
        ),
        migrations.AlterField(
            model_name="applicant",
            name="ht_in",
            field=models.FloatField(
                default=0, help_text="add your height in inches", verbose_name="height"
            ),
        ),
        migrations.AlterField(
            model_name="applicant",
            name="overstayed",
            field=models.BooleanField(
                default=False, verbose_name="have you overstayed in any country"
            ),
        ),
        migrations.AlterField(
            model_name="applicant",
            name="wt_ks",
            field=models.FloatField(blank=True, verbose_name="height in kilos"),
        ),
        migrations.AlterField(
            model_name="applicant",
            name="wt_lbs",
            field=models.FloatField(blank=True, verbose_name="height in pounds"),
        ),
    ]