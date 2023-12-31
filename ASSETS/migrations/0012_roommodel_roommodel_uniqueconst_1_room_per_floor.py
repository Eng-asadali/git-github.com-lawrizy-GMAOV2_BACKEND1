# Generated by Django 4.1.1 on 2022-09-24 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ASSETS", "0011_floormodel_floormodel_unique_floor_per_facility"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomModel",
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
                ("room", models.CharField(max_length=100)),
                (
                    "floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="room",
                        to="ASSETS.floormodel",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="roommodel",
            constraint=models.UniqueConstraint(
                fields=("room", "floor"), name="uniqueConst_1_room_per_floor"
            ),
        ),
    ]
