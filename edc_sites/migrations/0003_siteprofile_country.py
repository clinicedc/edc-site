# Generated by Django 2.2.11 on 2020-03-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_sites", "0002_auto_20190922_0452"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteprofile",
            name="country",
            field=models.CharField(max_length=250, null=True),
        ),
    ]