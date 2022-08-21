# Generated by Django 4.1 on 2022-08-21 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ASSETS", "0002_facility"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="ASSETS.company"
            ),
        ),
    ]
