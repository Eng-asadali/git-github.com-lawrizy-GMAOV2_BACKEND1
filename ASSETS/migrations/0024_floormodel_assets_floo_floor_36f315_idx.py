# Generated by Django 4.1.2 on 2022-12-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ASSETS", "0023_remove_roommodel_uniqueconst_1_room_per_floor_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="floormodel",
            index=models.Index(fields=["floor"], name="ASSETS_floo_floor_36f315_idx"),
        ),
    ]
