# Generated by Django 2.2.3 on 2019-09-09 18:59

import django.contrib.sites.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("sites", "0002_alter_domain_unique")]

    operations = [
        migrations.CreateModel(
            name="EdcSite",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": []},
            bases=("sites.site",),
            managers=[("objects", django.contrib.sites.models.SiteManager())],
        ),
        migrations.CreateModel(
            name="SiteProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, null=True)),
                ("description", models.TextField(null=True)),
                (
                    "site",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT, to="sites.Site"
                    ),
                ),
            ],
        ),
    ]
