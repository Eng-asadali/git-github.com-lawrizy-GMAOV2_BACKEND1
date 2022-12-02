# Generated by Django 4.1.2 on 2022-12-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ASSETS", "0020_alter_roomtypemodel_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomtypemodel",
            name="code",
            field=models.CharField(max_length=2),
        ),
        migrations.AddIndex(
            model_name="roomtypemodel",
            index=models.Index(
                fields=["room_type"], name="ASSETS_room_room_ty_1994af_idx"
            ),
        ),
    ]
