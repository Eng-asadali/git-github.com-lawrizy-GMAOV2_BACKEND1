# Generated by Django 4.1.1 on 2022-09-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ASSETS", "0007_alter_facility_city_alter_facility_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="image",
            field=models.ImageField(null=True, upload_to="static/pictures/facility"),
        ),
    ]