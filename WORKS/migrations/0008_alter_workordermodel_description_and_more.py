# Generated by Django 4.1.2 on 2022-10-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WORKS", "0007_remove_workordermodel_assigner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workordermodel",
            name="description",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="workordermodel",
            name="end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="workordermodel",
            name="start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]