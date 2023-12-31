# Generated by Django 4.1.1 on 2022-09-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ASSETS", "0006_alter_facility_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="city",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="facility",
            name="image",
            field=models.ImageField(null=True, upload_to="pictures/facility"),
        ),
        migrations.AlterField(
            model_name="facility",
            name="locality",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="facility", name="number", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="facility",
            name="postal_code",
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name="facility",
            name="street",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
