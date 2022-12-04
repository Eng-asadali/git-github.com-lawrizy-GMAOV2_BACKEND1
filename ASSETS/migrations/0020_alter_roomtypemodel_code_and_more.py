# Generated by Django 4.1.2 on 2022-12-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ASSETS", "0019_roomtypemodel_roommodel_number_roommodel_room_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomtypemodel",
            name="code",
            field=models.CharField(max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name="roomtypemodel",
            name="room_type",
            field=models.CharField(max_length=40, unique=True),
        ),
    ]