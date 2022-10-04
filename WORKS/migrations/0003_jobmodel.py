# Generated by Django 4.1.2 on 2022-10-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("WORKS", "0002_jobtypemodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                (
                    "domain",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="domain",
                        to="WORKS.domainmodel",
                    ),
                ),
                (
                    "job_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="job_type",
                        to="WORKS.jobtypemodel",
                    ),
                ),
            ],
        ),
    ]
