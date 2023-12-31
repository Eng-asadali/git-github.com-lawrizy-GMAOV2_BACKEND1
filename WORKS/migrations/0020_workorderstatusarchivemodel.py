# Generated by Django 4.2 on 2023-04-23 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WORKS', '0019_alter_workorderarchivemodel_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrderStatusArchiveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date_time', models.DateTimeField(blank=True, null=True)),
                ('status_before', models.CharField(blank=True, max_length=255, null=True)),
                ('status_after', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_order_status', to='WORKS.workorderarchivemodel')),
            ],
        ),
    ]
