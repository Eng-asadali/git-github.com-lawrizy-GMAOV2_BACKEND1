# Generated by Django 4.1.2 on 2023-01-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WORKS', '0015_workstatusmodel_works_works_name_7483e2_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrderPictureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='work_order_pictures')),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_order_pictures', to='WORKS.workordermodel')),
            ],
        ),
        migrations.AddIndex(
            model_name='workorderpicturemodel',
            index=models.Index(fields=['work_order', 'picture'], name='WORKS_worko_work_or_18f586_idx'),
        ),
    ]
