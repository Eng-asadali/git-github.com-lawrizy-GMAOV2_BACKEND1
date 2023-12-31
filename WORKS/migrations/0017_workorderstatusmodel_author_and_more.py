# Generated by Django 4.1.2 on 2023-02-13 10:42

import WORKS.models.work_models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WORKS', '0016_workorderpicturemodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorderstatusmodel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='author_wo_status', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workorderstatusmodel',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workorderpicturemodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=WORKS.models.work_models.work_order_picture_path),
        ),
    ]
