# Generated by Django 4.1.2 on 2022-10-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WORKS", "0004_rename_domain_jobmodel_domain_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobmodel",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="jobtypemodel",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]